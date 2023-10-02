import boto3
import json
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all
from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate

# initialization
session = boto3.session.Session()
client = session.client("bedrock-runtime")
# patch_all()

def handler(event, context):
    print(json.dumps(event))
    llm = Bedrock(
        client=client,
        model_id=event["model"],
        model_kwargs=event["model_kwargs"]
    )
    response = llm(event["prompt"])
    output = [line.strip() for line in response.split("\n\n")]
    print(json.dumps(output))
    return output
