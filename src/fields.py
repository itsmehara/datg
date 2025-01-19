import random

def define_field(name, data_type):
    value = generate_random_value(data_type)
    return {"name": name, "data_type": data_type, "value": value}


def get_supported_data_types():
    return ['int', 'str', 'float']


def generate_random_value(data_type):
    if data_type == 'int':
        return random.randint(0, 100)
    elif data_type == 'str':
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == 'float':
        return random.uniform(0.0, 100.0)
    else:
        raise ValueError("Unsupported data type")
