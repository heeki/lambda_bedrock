import json
from datetime import datetime
from lib.encoders import TimeDeltaEncoder

class Perf:
    def __init__(self, version, model):
        self.timer = datetime.now()
        self.version = version
        self.model = model

    def start(self):
        self.timer = datetime.now()

    def stop(self):
        diff = datetime.now() - self.timer
        return diff.total_seconds() * 1000

    def put_emf(self, aws_request_id, metric_name, duration):
        message = {
            "_aws": {
                "Timestamp": int(datetime.now().timestamp()),
                "CloudWatchMetrics": [
                    {
                        "Namespace": "LambdaBedrock",
                        "Dimensions": [["bedrockModel"]],
                        "Metrics": [{
                            "Name": metric_name,
                            "Unit": "Milliseconds",
                        }]
                    }
                ]
            },
            "functionVersion": self.version,
            "bedrockModel": self.model,
            "requestId": aws_request_id,
            f"{metric_name}": duration
        }
        print(json.dumps(message, cls=TimeDeltaEncoder))
