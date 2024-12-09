import logging
import uuid

from typing import List

def _filter_dict_by_keys(original_dict: dict, keys: List, required_keys: List = []):
    # Ensure all required keys are in the source dictionary
    missing_keys = [key for key in required_keys if key not in original_dict]
    if missing_keys:
        raise KeyError(f"Missing required parameter: {missing_keys}")
    
    # Create a new dictionary with only the key-value pairs where the key is in the list 'keys'
    return {key: original_dict[key] for key in keys if key in original_dict}


class WatsonxExternalPromptMonitoring:
    
        def __init__(self,
                 api_key: str,
                 space_id: str,
                 wml_url: str = "https://us-south.ml.cloud.ibm.com",
                 subscription_id: str = None
                 ) -> None:
            try:
                from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
                from ibm_aigov_facts_client import AIGovFactsClient
                from ibm_watson_openscale import APIClient as WosAPIClient
                from ibm_watsonx_ai import APIClient

            except ImportError:
                raise ImportError("""ibm-aigov-facts-client, ibm-watson-openscale or ibm-watsonx-ai not found, 
                                  please install it with `pip install ibm-aigov-facts-client ibm-watson-openscale ibm-watsonx-ai`""")

            self.subscription_id = subscription_id
            self._api_key = api_key
            self._space_id = space_id
            self._wml_url = wml_url
            
                    
        def _create_detached_prompt(self):
            from ibm_aigov_facts_client import DetachedPromptTemplate, PromptTemplate, AIGovFactsClient
            
            try:
                _aigov_client = AIGovFactsClient(
                    api_key=self._api_key,
                    container_id=self._space_id,
                    container_type="space",
                    disable_tracing=True
                    )
                
            except Exception as e:
                logging.error(f"Error connecting to IBM factsheets: {e}")
                raise
            
            detached_information = DetachedPromptTemplate(**self.detached_details)
            prompt_template = PromptTemplate(**self.prompt_details)

            created_pta = _aigov_client.assets.create_detached_prompt(
               **self.external_prompt,
                prompt_details=prompt_template,
                detached_information=detached_information)
            
            return created_pta.to_dict()["asset_id"]
            
            
        def _create_deployment_pta(self, asset_id: str):
            from ibm_watsonx_ai import APIClient
            
            try:
                _wml_client = APIClient({
                        "url": self._wml_url,
                        "apikey": self._api_key 
                        })
                _wml_client.set.default_space(self._space_id)
                
            except Exception as e:
                logging.error(f"Error connecting to IBM watsonx.ai: {e}")
                raise
            
            meta_props = {
                _wml_client.deployments.ConfigurationMetaNames.PROMPT_TEMPLATE: { "id" : asset_id },
                _wml_client.deployments.ConfigurationMetaNames.DETACHED: {},
                _wml_client.deployments.ConfigurationMetaNames.BASE_MODEL_ID: self.detached_details['model_id'],
                _wml_client.deployments.ConfigurationMetaNames.NAME: self.external_prompt['name'] + " " + "deployment"
            }
            
            created_deployment = _wml_client.deployments.create(asset_id, meta_props)
            
            return _wml_client.deployments.get_uid(created_deployment)
        
            
        def create_prompt_monitor(self, prompt_metadata: dict, 
                                  context_fields: List,
                                  question_field: str):
            from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
            from ibm_watson_openscale import APIClient as WosAPIClient
            
            try:
                authenticator = IAMAuthenticator(apikey=self._api_key)
                self._wos_client = WosAPIClient(authenticator=authenticator)
                
            except Exception as e:
                logging.error(f"Error connecting to IBM openscale: {e}")
                raise
                
            self.prompt_details = _filter_dict_by_keys(prompt_metadata, 
                                                       ["model_version", "prompt_variables", "prompt_instruction",
                                                        "input_prefix", "output_prefix", "input", "model_parameters"])
            self.detached_details = _filter_dict_by_keys(prompt_metadata, 
                                                       ["model_id", "model_provider", "model_name", 
                                                        "model_url", "prompt_url", "prompt_additional_info"],
                                                       ["model_id", "model_provider"])
            self.detached_details['prompt_id'] = "detached_prompt" + str(uuid.uuid4())
            self.external_prompt = _filter_dict_by_keys(prompt_metadata, 
                                                       ["name", "model_id", "task_id", "description", "container_id"],
                                                       ["name", "model_id", "task_id"])
            
            pta_uid = self._create_detached_prompt()
            deployment_uid =  self._create_deployment_pta(asset_id=pta_uid)
            
            monitors = {
                "generative_ai_quality": {
                "parameters": {
                    "min_sample_size": 10,
                    "metrics_configuration":{}
                    }
                }}
            
            generative_ai_monitor_details = self._wos_client.wos.execute_prompt_setup(prompt_template_asset_id = pta_uid, 
                                                                   space_id = self._space_id,
                                                                   deployment_id = deployment_uid,
                                                                   label_column = "reference_output",
                                                                   context_fields=context_fields,     
                                                                   question_field = question_field,   
                                                                   operational_space_id = "production", 
                                                                   problem_type = self.external_prompt['task_id'],
                                                                   input_data_type = "unstructured_text", 
                                                                   supporting_monitors = monitors, 
                                                                   background_mode = False).result

            generative_ai_monitor_details = generative_ai_monitor_details._to_dict()
            self.subscription_uid = generative_ai_monitor_details["subscription_id"]
            
            return self.subscription_uid
             
                    
        def payload_logging(self):
            pass