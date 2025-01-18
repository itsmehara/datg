# datg
DatG is a Data Generation Lib to generate dynamic data developed in python.


# DatG: Dynamic Data Generation Library

## Overview
DatG is a Python-based dynamic data generation library designed to create synthetic data in various formats like CSV and JSON. It allows users to specify fields and the number of records to generate, making it highly customizable for testing and development purposes.

## Features
- Generate data in CSV or JSON formats.
- Dynamic field customization: Users can define the number of fields and corresponding data types.
- Supports generation of a specified number of records.
- Extendable to other data formats in the future.

## Modules

### 1. `datg.generator`
Handles the core data generation logic.

#### Functions:
- `generate_data(fields: list, num_records: int, format: str) -> str`
  - **Description**: Generates synthetic data based on user-defined fields and the number of records.
  - **Parameters**:
    - `fields`: List of field names.
    - `num_records`: Number of records to generate.
    - `format`: Output format ('csv' or 'json').
  - **Returns**: Generated data in the specified format.

### 2. `datg.fields`
Manages the data types and field definitions.

#### Functions:
- `define_field(name: str, data_type: str) -> dict`
  - **Description**: Defines a new field with a specified data type.
  - **Parameters**:
    - `name`: Name of the field.
    - `data_type`: Data type of the field (e.g., `int`, `str`, `float`).
  - **Returns**: Field definition as a dictionary.

- `get_supported_data_types() -> list`
  - **Description**: Returns a list of supported data types.
  - **Returns**: List of supported data types.

### 3. `datg.formatters`
Responsible for formatting the generated data into the specified output format.

#### Functions:
- `to_csv(data: list) -> str`
  - **Description**: Converts generated data to CSV format.
  - **Parameters**:
    - `data`: List of dictionaries representing the data.
  - **Returns**: CSV formatted string.

- `to_json(data: list) -> str`
  - **Description**: Converts generated data to JSON format.
  - **Parameters**:
    - `data`: List of dictionaries representing the data.
  - **Returns**: JSON formatted string.

### 4. `datg.utils`
Utility functions to support various operations in the library.

#### Functions:
- `validate_format(format: str) -> bool`
  - **Description**: Validates if the specified format is supported.
  - **Parameters**:
    - `format`: Output format to validate.
  - **Returns**: Boolean indicating if the format is supported.

- `generate_random_value(data_type: str) -> Any`
  - **Description**: Generates a random value based on the specified data type.
  - **Parameters**:
    - `data_type`: Data type for which to generate a value.
  - **Returns**: Random value of the specified data type.

## Future Enhancements
- Support for additional data formats (e.g., XML, Excel).
- More complex data type support (e.g., nested objects, arrays).
- Field-specific customization options (e.g., ranges for numeric fields, regex for string fields).

## Installation
```bash
pip install datg
```

## Usage
```python
from datg.generator import generate_data

fields = ['name', 'age', 'email']
num_records = 10
format = 'csv'

data = generate_data(fields, num_records, format)
print(data)
```

## Contributing
Contributions are welcome! Please follow the [contribution guidelines](CONTRIBUTING.md) to submit issues and pull requests.

## License
DatG is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
