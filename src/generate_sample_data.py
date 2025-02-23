from generator import generate_data


FIELD_SCHEMA_LIST = [
    ("name", "str"),
    ("age", "int"),
    ("email", "str"),
    ("phone_number", "str"),
    ("address", "str"),
    ("date_of_birth", "str"),
    ("gender", "str"),
    ("nationality", "str"),
    ("marital_status", "str"),
    ("emergency_contact", "str"),
    ("salary", "float"),
    ("department", "str"),
    ("joining_date", "str"),
    ("performance_score", "int"),
    ("manager", "str"),
    ("location", "str"),
    ("project_count", "int"),
    ("employee_id", "str"),
    ("employment_type", "str"),
    ("experience_years", "int"),
    ("job_title", "str"),
    ("work_location", "str"),
    ("team", "str"),
    ("shift_timing", "str"),
    ("reporting_manager", "str"),
    ("bonus", "float"),
    ("stock_options", "int"),
    ("last_promotion_date", "str"),
    ("performance_rating", "int"),
    ("attendance_score", "int"),
    ("overtime_hours", "int"),
    ("employee_email", "str"),
    ("system_access_level", "str"),
    ("device_assigned", "str"),
    ("vpn_access", "bool"),
    ("joining_bonus", "float"),
    ("resignation_date", "str"),
    ("exit_interview_feedback", "str"),
    ("termination_reason", "str"),
    ("work_permit_status", "str"),
    ("certifications", "list"),
    ("languages_known", "list"),
    ("projects_handled", "list"),
    ("training_completed", "list")
]


def test_all_fields():
    """
    Generate and print a sample record covering all defined fields.
    """
    num_records = 2
    format = 'csv'
    # fields = list(FIELD_SCHEMA.keys())  # Extract all field names
    # test_record = {field: generate_random_value(field, FIELD_SCHEMA[field]) for field in fields}
    test_records = generate_data(FIELD_SCHEMA_LIST, num_records, format)

    print("🔹 Sample Test Record Covering All Fields:")
    print(test_records)  # Print to verify


def main():
    fields = [
        ('name', 'str'),
        ('age', 'int'),
        ('email', 'str'),
        ('salary', 'float'),
        ('department', 'str'),
        ('joining_date', 'str'),
        ('performance_score', 'int'),
        ('manager', 'str'),
        ('location', 'str'),
        ('project_count', 'int'),
        ('gender', 'str'),
        ('phone_number', 'int')
    ]
    num_records = 10000
    format = 'csv'  # Change to 'json' if needed

    result = generate_data(FIELD_SCHEMA_LIST, num_records, format)
    with open(f"output.{format}", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()
    # # Call the test function
    # test_all_fields()