from generator import generate_data

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
        ('project_count', 'int')
    ]
    num_records = 10000
    format = 'csv'  # Change to 'json' if needed

    result = generate_data(fields, num_records, format)
    with open(f"output.{format}", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()