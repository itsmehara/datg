import random
from typing import Dict, Any, Optional
from faker import Faker

fake = Faker()
# Custom list of 30+ companies
COMPANIES = [
    "Google", "Microsoft", "Amazon", "Apple", "Facebook", "Tesla", "IBM", "Oracle",
    "Salesforce", "Netflix", "Uber", "Airbnb", "Adobe", "Intel", "Cisco", "Spotify",
    "Dell", "HP", "NVIDIA", "Samsung", "LinkedIn", "Zoom", "Red Hat", "SAP", "Twitter",
    "PayPal", "Visa", "Mastercard", "Goldman Sachs", "JP Morgan", "Morgan Stanley"
]

DEPARTMENTS = [
    "Human Resources", "Finance", "Marketing", "Sales", "IT Support", "Software Development",
    "Data Science", "Cybersecurity", "Cloud Engineering", "DevOps", "AI & Machine Learning",
    "Business Intelligence", "Product Management", "Project Management", "Customer Service",
    "Technical Support", "Research & Development", "Operations", "Supply Chain Management",
    "Procurement", "Quality Assurance", "Risk Management", "Compliance", "Legal", "Administration",
    "Corporate Strategy", "Public Relations", "Social Media Marketing", "Content Marketing",
    "UX/UI Design", "Graphic Design", "Mobile App Development", "Embedded Systems",
    "Network Engineering", "Database Administration", "IT Infrastructure", "Manufacturing",
    "Logistics", "Retail Management", "Healthcare Services", "Pharmaceuticals", "Education & Training",
    "Energy & Utilities", "Telecommunications", "Banking & Investments", "Insurance", "Real Estate",
    "Media & Entertainment", "Aerospace & Defense", "Automotive Engineering"
]


def define_field(name: str, data_type: str) -> Dict[str, Any]:
    """
    Define a field with a name and data type.

    Args:
        name (str): Field name.
        data_type (str): Data type of the field.

    Returns:
        Dict[str, Any]: A dictionary with field details.
    """
    value = generate_random_value(data_type, name)
    return {"name": name, "data_type": data_type, "value": value}


def get_supported_data_types() -> list[str]:
    """
    Get a list of supported data types.

    Returns:
        List[str]: Supported data types.
    """
    return ['int', 'str', 'float']


def generate_random_value(data_type: str, field_name_: Optional[str] = None) -> Any:
    """
    Generate a random value based on the data type and field name.

    Args:
        data_type (str): The data type for which to generate a value.
        field_name (Optional[str]): The specific field name, if applicable.

    Returns:
        Any: A random value of the specified data type.
    """
    field_name = field_name_.lower()
    if field_name == "name":
        return fake.name()
    elif field_name == "email":
        return fake.email()
    elif field_name == "job":
        return fake.job()
    elif field_name == "company":
        return random.choice(COMPANIES)  # Pick a random company from the list
    elif field_name == "location":
        return fake.city()
    elif field_name == "joining_date":
        return fake.date_between(start_date="-10y", end_date="today").strftime("%Y-%m-%d")
    elif field_name == "salary":
        return round(random.uniform(30000.0, 200000.0), 2)
    elif field_name == "performance_score":
        return random.randint(1, 10)
    elif field_name == "project_count":
        return random.randint(0, 20)
    elif field_name == "age":
        return random.randint(21, 71)
    elif field_name == "department":
        return random.choice(DEPARTMENTS)
    elif field_name == "manager":
        return fake.name()
    # elif field_name == "location":
    #     return random.choice(DEPARTMENTS)
    elif data_type == "int":
        return random.randint(0, 100)
    elif data_type == "str":
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == "float":
        return random.uniform(0.0, 100.0)
    else:
        raise ValueError("Unsupported data type")
