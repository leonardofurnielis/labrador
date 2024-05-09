import os
import re
import tempfile
import ibm_boto3

from typing import List
from pydantic import BaseModel, Field
from ibm_botocore.client import Config

from spyder_index.core.document import Document
from spyder_index.readers.directory import DirectoryReader

class IBMS3Reader(BaseModel):
    bucket: str = Field(default="")
    ibm_api_key_id: str = Field(default="")
    ibm_service_instance_id: str = Field(default="")
    s3_endpoint_url: str = Field(default="")

    def load_data(self) -> List[Document]: 

        ibm_s3 = ibm_boto3.resource(
            "s3",
            ibm_api_key_id=self.ibm_api_key_id,
            ibm_service_instance_id=self.ibm_service_instance_id,
            config=Config(signature_version='oauth'),
            endpoint_url=self.s3_endpoint_url,
        )

        bucket = ibm_s3.Bucket(self.bucket)

        with tempfile.TemporaryDirectory() as temp_dir:
            for obj in bucket.objects.filter(Prefix=""):
                file_path = f"{temp_dir}/{obj.key}"
                os.makedirs(os.path.dirname(file_path), exist_ok=True)
                ibm_s3.meta.client.download_file(self.bucket, obj.key, file_path)
                    
            s3_source = re.sub(r"^(https?)://", "", self.s3_endpoint_url)
            
            return DirectoryReader(input_dir=temp_dir, extra_info={"source": f"{s3_source}/{self.bucket}"}).load_data()

