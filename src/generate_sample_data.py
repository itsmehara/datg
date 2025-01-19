# Import the generate_data function from the datg.generator module
from datg.generator import generate_data

# Define the fields and their corresponding data types
fields = [
    ('name', 'str'),
    ('age', 'int'),
    ('email', 'str'),
    ('country', 'str'),
    ('city', 'str'),
    ('zip_code', 'str'),
    ('phone_number', 'str'),
    ('dob', 'str'),
    ('salary', 'float'),
    ('department', 'str')
]

# Specify the number of records to generate
num_records = 10000

# Choose the output format ('json' or 'csv')
output_format = 'csv'  # Change to 'json' for JSON output

# Generate the data
generated_data = generate_data(fields, num_records, output_format)

# Save the generated data to a file
if output_format == 'csv':
    with open('output.csv', 'w') as f:
        f.write(generated_data)
    print("Data saved to output.csv")
else:
    with open('output.json', 'w') as f:
        f.write(generated_data)
    print("Data saved to output.json")
