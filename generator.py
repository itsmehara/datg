import json
import csv
from .formatters import to_csv, to_json
from .fields import define_field


def generate_data(fields, num_records, format):
    data = []
    for _ in range(num_records):
        record = {}
        for field in fields:
            name, data_type = field
            record[name] = define_field(name, data_type)['value']
        data.append(record)

    if format == 'csv':
        return to_csv(data)
    elif format == 'json':
        return to_json(data)
    else:
        raise ValueError("Unsupported format")
