import json
import csv
from typing import List, Tuple, Union
from formatters import to_csv, to_json
from fields import define_field

def generate_data(fields: List[Tuple[str, str]], num_records: int, format: str) -> Union[str, None]:
    """
    Generate data based on specified fields and format.
    
    Args:
        fields (List[Tuple[str, str]]): List of field names and their data types.
        num_records (int): Number of records to generate.
        format (str): Output format, either 'csv' or 'json'.

    Returns:
        Union[str, None]: Generated data in specified format.
    """
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