import boto3
import json
from aws_lambda_powertools import Metrics
from aws_lambda_powertools.metrics import MetricUnit
# from aws_xray_sdk.core import xray_recorder
# from aws_xray_sdk.core import patch_all
from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate
from lib.perf import Perf

# initialization
session = boto3.session.Session()
client = session.client("bedrock-runtime")
# patch_all()
metrics = Metrics()

@metrics.log_metrics
def handler(event, context):
    print(json.dumps(event))
    perf = Perf(context.function_version, event["model"])
    metrics.add_dimension(name="bedrockModel", value=event["model"])

    perf.start()
    llm = Bedrock(
        client=client,
        model_id=event["model"],
        model_kwargs=event["model_kwargs"]
    )
    duration = perf.stop()
    # perf.put_emf(context.aws_request_id, "initDuration", duration)
    metrics.add_metric(name="initDuration", unit=MetricUnit.Milliseconds, value=duration)

    perf.start()
    response = llm(event["prompt"])
    duration = perf.stop()
    # perf.put_emf(context.aws_request_id, "invokeDuration", duration)
    metrics.add_metric(name="invokeDuration", unit=MetricUnit.Milliseconds, value=duration)

    output = [line.strip() for line in response.split("\n\n")]
    print(json.dumps(output))
    return output
