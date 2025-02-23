import json
import csv
from typing import List, Dict
from io import StringIO


def to_csv(data: List) -> str:
    """
    Convert a list of dictionaries to CSV format.
    
    Args:
        data (List[Dict[str, Any]]): List of records to convert.

    Returns:
        str: CSV formatted string.
    """
    if not data:
        return ""

    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)
    return output.getvalue()


def to_json(data: List) -> str:
    """
    Convert a list of dictionaries to JSON format.
    
    Args:
        data (List[Dict[str, Any]]): List of records to convert.

    Returns:
        str: JSON formatted string.
    """
    return json.dumps(data, indent=2)