import json
import csv
from io import StringIO


def to_csv(data):
    if not data:
        return ""

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def to_json(data):
    return json.dumps(data, indent=4)
