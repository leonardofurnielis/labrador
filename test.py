from tempestai.monitor import WatsonxExternalPromptMonitoring

prompt_monitor = WatsonxExternalPromptMonitoring(api_key="pSvblNaWfSIkFlA_rE3cyVdYZ3mzxD6oNZHCBc4UNE1B", 
                                                 space_id="682047e7-05f9-491f-9f6f-f1e36ddfd2d7")


prompt_input="""
[INST] <>You are an assistant named Buddy who helps customers of an Australian online-only insurer named Bingle. Being online only, you should not suggest contacting Bingle. You should only answer queries related to car insurance. Your answer must be general in nature. You should only use provided information from the document to generate your answer. If the answer to the question is not in the provided document reply with,  "I am sorry but unfortunately I do not have information to help you.".  Use Australian spelling and Australian insurance terminology. If you do not respond in the persona of Buddy, users who are on the Bingle website will be confused. You should maintain a friendly customer service tone.<> 
    Here is the document you should use to answer the user:
    {context1}\n{context2}\n{context3}
    Here are some important rules for the interaction:
    - Always stay in character, as Buddy from Bingle and answer user questions in first person.
    - If you are unsure how to respond, say “I am sorry but unfortunately I do not have information to help you.”.
    - If someone asks something irrelevant, say, “Sorry, I am Buddy and I can help with Car Insurance. Do you have an insurance related question today I can help you with?”.
    - Never mention or suggest calling, emailing, writing or contacting customer services or Bingle.
    - If the answer is not in the document answer with: "I am sorry but unfortunately I do not have information to help you.”.
    - If the document provides instruction ensure to list them out so that the user understands the process to take, this will be extremly helpful.
    - If no insurance cover type (comprehensive or third party cover) is mentioned in the user question then always provide an answer for both types of cover".
    - If a specific type of insurance cover (comprehensive or third party cover) is mentioned in the user question then respond with an answer only for that cover type.
    - Remember, user have already looked at the Bingle website so do not suggest them to check our website as this will be condescending and rude, instead suggest they review the Product Disclosure Statement (PDS).
    
    Here is an example of how to respond in a standard interaction:
    Users question: Hi, how were you created and what do you do? [/INST]
    Step 1: Check if the question is related to Bingle car insurance. Yes, the question is related to car insurance, specifically the insurance Buddy that is me.
    Step 2: Check if the answer can be found in the provided document. The context does mention information about Buddy and how I am an AI assistant to help them.
    Step 3: Provide the answer in structured json. 
    ANSWER: {{"answer": "Hello! My name is Buddy, and I was created by Bingle to help you with information about Bingles insurance services. What can I help you with today?."}} 
    [INST]
    Here is another example of how to respond in a standard interaction:
    Users question: Hi can I get housing insurance? [/INST]
    Step 1: Check if the question is related to Bingle car insurance. No, the question is not related to car insurance.
    Step 2: Check if the answer can be found in the provided document. The document does not mention information about housing insurance.
    Step 3: Provide the answer in structured json. 
    ANSWER: {{"answer": "I'm sorry, but unfortunately I don't have information to help you with that question."}}
    [INST] 
    Here is another example of how to respond in a standard interaction:
    Users question: Hi does Bingle offer a rental car while my car is being repaired? [/INST]
    Step 1: Check if the question is related to Bingle car insurance. Yes, the question is related to car insurance, specifically the getting a rental car while their car is being repaired.
    Step 2: Check if the answer can be found in the provided document. The document does mention information about rental cars and how they are provided in the comprehensive policy with the Keep Mobile option.
    Step 3: Provide the answer in structured json. 
    ANSWER: {{"answer": "Yes I can help with that, for an extra premium our Comprehensive Policy offers a Keep Mobile option which includes unlimited, car hire and Copycat cover. Our Third Party Policy does not include the Keep Mobile option. I hope this information helps for further details please review the Product Disclosure Statement (PDS)"}}
    [INST] 
    Please think step by step when the user asks you a question and decide if the content is actually in the document provided. Work through these steps, then provide the answer in structured json format.
    
    User Question: {question} [/INST]
    Step 1: Check if the question is related to Bingle car insurance.

"""
# import ibm_watson_openscale
 
# print(ibm_watson_openscale.__version__)

# sub_uid = prompt_monitor.create_prompt_monitor({"prompt_variables":{"context1": "","context2": "","context3": "","question": ""},
#                                       "model_id":"meta-llama/llama-3-70b-instruct",
#                                       "model_provider":"Meta",
#                                       "model_name":"llama-3-70b-instruct",
#                                       "model_url":"https://us-south.ml.cloud.ibm.com/ml/v1/deployments/insurance_test_deployment/text/generation?version=2021-05-01",
#                                       "task_id":"retrieval_augmented_generation",
#                                       "input":prompt_input,
#                                       "description":"Detached prompt sample - from tempestai",
#                                       "name":"External prompt sample - from tempestai"
#                                       }, ["context1", "context2","context3"], "question")

# print(sub_uid)

data = [
    {'context1': "\n<t1></t1>\nAt Bingle, we don't have the option to change your policy from Comprehensive to Third Party Property Damage, or vice versa. If you want to change the level of cover, youâ€™ll need to start up a NEW Comprehensive Insurance (https://online.bingle.com.au/motor/pub/binglequote?productType=comprehensive) or Third Party Property Damage (https://online.bingle.com.au/motor/pub/binglequote?productType=thirdParty) policy online, and cancel (https://online.bingle.com.au/onesuncorp) the existing policy. Cancelling within the cooling off period. If you change your mind within 21 days of when your policy starts, and you haven't made a claim, you can cancel your policy and receive a full refund. Just make sure you select 'Cooling off' as the reason for the cancellation, and select the start date of your policy as the cancellation date. If a refund is due to you, this will automatically be issued back to the original card you used to pay for the policy. To cancel your policy please follow our instructions here: I need to cancel my policy. (https://help.bingle.com.au/hc/en-us/articles/20727718 8) Cancelling after the cooling off period. After the cooling off period you can still cancel your policy, and we'll refund the unexpired portion of your premium, less any non-refundable government charges, if the refund is more than $1\n", 
     'context2': "\n<t2></t2>\nWeâ€™re sorry to hear your car has been written off. Hopefully youâ€™re back on the road ASAP with some new wheels to get you around. Until then, you may be worried about your policy taking any more payments and are in a hurry to stop the payments. There are two ways that cars can be deemed a total loss (written off): by Bingle, or by the other personâ€™s insurer. Who is doing the writing off will determine what you need to do next. 1 - Total Loss by Bingle If the vehicle has been written off by Bingle, you do not need to do anything. If you have New for Old cover, then weâ€™ll organise the replacement and the policy will continue (more info about that can be found here (https://help.bingle.com.au/hc/en-us/articles/115008068468-What-is-New-for-Old-)). If you donâ€™t have New for Old cover, when your claim is settled, Bingle will organise for your policy to be cancelled. If you pay monthly, any remaining debits left owing are deducted from the final settlement, so if any other payments are taken before the cancellation occurs, these will simply be applied against the deduction. More information about this can be found in our Comprehensive Car Insurance PDS (https://www.bingle.com.au/documents/disclosures/comp_pds_2021031 6.pdf) on Page 16 under the heading When your car is a total loss. 2 - Total Loss by another insurer If your car has been involved in an accident and your car was assessed and deemed to be a total loss through the other partyâ€™s insurance, they do not notify us of this. It is important that you process the insurance policy cancellation yourself. This car be done via Bingle Self-Service here (https://online.bingle.com.au/onesuncorp). Alternatively, if youâ€™ve already got a new car, you can swap it out here (https://online.bingle.com.au/onesuncorp). Iâ€™ve scrapped my car You may also decide that your car is no longer worth keeping and you decide to scrap it. Cancelling the registration does not cancel the Comprehensive or Third Party insurance policy, so you will need to cancel the policy. This can be done via Bingle Self-Service. (https://online.bingle.com.au/onesuncorp) For instructions on how to do this, check out 'How do I cancel my policy?' (https://help.bingle.com.au/hc/en-us/articles/207277188-How-do-I-cancel-my-policy-).\n",
     'context3': "\n<t3></t3>\nCompulsory Third Party Insurance, or â€˜Green Slipâ€™ as itâ€™s known in New South Wales and â€˜MAIâ€™ in the Australian Capital Territory, is a mandatory type of insurance that you purchase along with your vehicle registration. This isnâ€™t the same as Third Party Car Insurance. In most states, CTP/MAI is included with your registration fees, however if youâ€™re in New South Wales or the Australian Capital Territory, youâ€™ll have the option to nominate which insurer will provide your CTP/MAI cover when you pay for your registration. CTP/MAI Insurance can cover you or the other driverâ€™s liability if someone is injured in an accident â€“ be it you, other drivers, passengers, pedestrians, or cyclists. Bingle doesnâ€™t offer CTP Insurance, however you can purchase it from AAMI (https://www.aami.com.au/ctp-insurance.html) or GIO (https://www.gio.com.au/ctp-insurance/nsw-ctp-green-slip.html). Third Party Car Insurance (https://www.bingle.com.au/car-insurance/third-party-car-insurance.html), on the other hand, is a level of insurance that only covers damage you cause to other peopleâ€™s car and property, i.e. damage caused by your car, but not your legal liability for injuries. What do I do If I purchased Third Party Car Insurance instead of CTP? Bingle doesnâ€™t offer CTP insurance, so if youâ€™ve purchased Third Party Car Insurance from us and tried to register it with your state or territoryâ€™s road authority as CTP Insurance, you wonâ€™t be allowed to register. If you need to cancel your Third Party Car Insurance, head to Bingle Self-Service (https://online.bingle.com.au/onesuncorp) and cancel your policy. If you cancel your policy within 21 days of purchasing it â€“ and you havenâ€™t made a claim â€“ you could be eligible for our cooling off period, where you can cancel your policy and receive a full refund. Read this article for more information on our cooling off period https://help.bingle.com.au/hc/en-us. The information is intended to be of general nature only. Subject to any rights you may have under any law, we do not accept any legal responsibility for any loss or damage, including loss of business or profits or any other indirect loss, incurred as a result of reliance upon the information. Please make your own enquiries.\n", 
     'question': "After cancelling policy , how long we have to launch a claim for third party damages if accident happened before cancellation of policy", 'generated_text': "If you cancel your policy, you can still make a claim for third party damages if the accident happened before the cancellation of your policy. You have up to 3 years from the date of the accident to make a claim."},
    # Adicione mais registros conforme necessário
]

prompt_monitor.payload_logging(data=data, subscription_id="2fab9f59-25a1-40ba-a217-987028c0ae0f")