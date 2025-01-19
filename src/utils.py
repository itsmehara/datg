from typing import bool

def validate_format(format: str) -> bool:
    """
    Validate the output format.
    
    Args:
        format (str): Format to validate.

    Returns:
        bool: True if format is valid, else False.
    """
    return format in ['csv', 'json']