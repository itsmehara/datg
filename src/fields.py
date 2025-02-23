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
        return random.choice(COMPANIES)
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
        return random.randint(21, 70)  # Fixed range 21-70
    elif field_name == "department":
        return random.choice(DEPARTMENTS)
    elif field_name == "manager":
        return fake.name()
    elif field_name == "phone_number":
        return fake.phone_number()
    elif field_name == "address":
        return fake.address()
    elif field_name == "date_of_birth":
        return fake.date_of_birth(minimum_age=21, maximum_age=70).strftime("%Y-%m-%d")
    elif field_name == "gender":
        return random.choice(["Male", "Female"]*30 + ["Non-binary", "Other"])
    elif field_name == "nationality":
        return fake.country()
    elif field_name == "marital_status":
        return random.choice(["Single", "Married", "Divorced", "Widowed"])
    elif field_name == "emergency_contact":
        return fake.phone_number()
    elif field_name == "employee_id":
        return fake.uuid4()
    elif field_name == "employment_type":
        return random.choice(["Full-time", "Part-time", "Contract", "Intern"])
    elif field_name == "experience_years":
        return random.randint(0, 40)
    elif field_name == "job_title":
        return fake.job()
    elif field_name == "work_location":
        return random.choice(["Office", "Remote", "Hybrid"])
    elif field_name == "team":
        return fake.word().capitalize() + " Team"
    elif field_name == "shift_timing":
        return random.choice(["Morning", "Evening", "Night"])
    elif field_name == "reporting_manager":
        return fake.name()
    elif field_name == "bonus":
        return round(random.uniform(5000, 50000), 2)
    elif field_name == "stock_options":
        return random.randint(0, 1000)
    elif field_name == "last_promotion_date":
        return fake.date_between(start_date="-5y", end_date="today").strftime("%Y-%m-%d")
    elif field_name == "performance_rating":
        return random.randint(1, 5)
    elif field_name == "attendance_score":
        return random.randint(50, 100)
    elif field_name == "overtime_hours":
        return random.randint(0, 50)
    elif field_name == "employee_email":
        return fake.company_email()
    elif field_name == "system_access_level":
        return random.choice(["Admin", "Employee", "Manager", "Intern"])
    elif field_name == "device_assigned":
        return random.choice(["MacBook Pro", "Dell XPS", "ThinkPad", "HP EliteBook"])
    elif field_name == "vpn_access":
        return random.choice([True, False])
    elif field_name == "joining_bonus":
        return round(random.uniform(10000, 50000), 2)
    elif field_name == "resignation_date":
        return fake.date_between(start_date="-3y", end_date="today").strftime("%Y-%m-%d") if random.random() < 0.3 else None
    elif field_name == "exit_interview_feedback":
        return fake.sentence()
    elif field_name == "termination_reason":
        return random.choice(["Resigned", "Performance Issue", "Layoff", "Contract Ended", "Retired"])
    elif field_name == "work_permit_status":
        return random.choice(["Valid", "Expired", "Not Required"])
    elif field_name == "certifications":
        return [fake.word().capitalize() + " Certification" for _ in range(random.randint(0, 3))]
    elif field_name == "languages_known":
        return random.sample(["English", "French", "Spanish", "German", "Mandarin", "Japanese", "Hindi", "Arabic"], random.randint(1, 3))
    elif field_name == "projects_handled":
        return [fake.bs().capitalize() for _ in range(random.randint(1, 5))]
    elif field_name == "training_completed":
        return [fake.sentence() for _ in range(random.randint(0, 2))]
    elif data_type == "int":
        return random.randint(0, 100)
    elif data_type == "str":
        return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
    elif data_type == "float":
        return random.uniform(0.0, 100.0)
    else:
        raise ValueError(f"Unsupported field: {field_name}")
