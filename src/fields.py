import random
from typing import Dict, Any

def define_field(name: str, data_type: str) -> Dict[str, Any]:
    """
    Define a field with a name and data type.
    
    Args:
        name (str): Field name.
        data_type (str): Data type of the field.

    Returns:
        Dict[str, Any]: A dictionary with field details.
    """
    value = generate_random_value(data_type)
    return {"name": name, "data_type": data_type, "value": value}


def get_supported_data_types() -> List[str]:
    """
    Get a list of supported data types.
    
    Returns:
        List[str]: Supported data types.
    """
    return ['int', 'str', 'float']


def generate_random_value(data_type: str) -> Any:
    """
    Generate a random value based on the data type.
    
    Args:
        data_type (str): The data type for which to generate a value.

    Returns:
        Any: A random value of the specified data type.
    """
    if data_type == 'int':
        return random.randint(0, 100)
    elif data_type == 'str':
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == 'float':
        return random.uniform(0.0, 100.0)
    else:
        raise ValueError("Unsupported data type")