## Overview
This repository implements a quick prototype with AWS Lambda and Amazon Bedrock.

## Troubleshooting
Needed to enable access to the Anthropic Claude model before invoking the function. Got the following error.
```json
{
  "errorMessage": "Error raised by bedrock service: An error occurred (AccessDeniedException) when calling the InvokeModel operation: Your account is not authorized to invoke this API operation.",
  "errorType": "ValueError",
  "requestId": "c6692e10-7513-47b1-885b-015174d150f7",
  "stackTrace": [
    "  File \"/var/task/fn.py\", line 39, in handler\n    response = llm(event[\"prompt\"])\n",
    "  File \"/opt/python/langchain/llms/base.py\", line 878, in __call__\n    self.generate(\n",
    "  File \"/opt/python/langchain/llms/base.py\", line 658, in generate\n    output = self._generate_helper(\n",
    "  File \"/opt/python/langchain/llms/base.py\", line 546, in _generate_helper\n    raise e\n",
    "  File \"/opt/python/langchain/llms/base.py\", line 533, in _generate_helper\n    self._generate(\n",
    "  File \"/opt/python/langchain/llms/base.py\", line 1053, in _generate\n    self._call(prompt, stop=stop, run_manager=run_manager, **kwargs)\n",
    "  File \"/opt/python/langchain/llms/bedrock.py\", line 383, in _call\n    return self._prepare_input_and_invoke(prompt=prompt, stop=stop, **kwargs)\n",
    "  File \"/opt/python/langchain/llms/bedrock.py\", line 237, in _prepare_input_and_invoke\n    raise ValueError(f\"Error raised by bedrock service: {e}\")\n"
  ]
}
```

Had issues with unzipped package size (including layers).

| Layer                        | Include | ReportedSize(B) | ReportedSize(M) | UncompressedSize(K) | UncompressedSize(M) |
|------------------------------|---------|-----------------|-----------------|---------------------|---------------------|
| xray-python3:3               | yes     | 13,749,690      | 13.11           | 87,552              | 85.50               |
| LambdaInsightsExtension:38   | no      | 4,198,176       | 4.00            |                     | 0.00                |
| langchain:5 (boto3==1.28.57) | yes     | 41,742,613      | 39.81           | 194,192             | 189.64              |
| Total                        |         | 55,492,303      | 52.92           | 281,744             | 275.14              |