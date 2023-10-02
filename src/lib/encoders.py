import json
from datetime import datetime, timedelta
from decimal import Decimal

class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return json.JSONEncoder.default(self, o)

class TimeDeltaEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, timedelta):
            return o.total_seconds() * 1000
        return json.JSONEncoder.default(self, o)