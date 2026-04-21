import sys

def get_emails(filepath: str) -> list[list[str]]:
    employees = list()
    with open(filepath, 'r', encoding='utf-8') as file:

        for row_number, email in enumerate(file, start=1):
            email = email.strip()
            if not email:
                continue
            
            parts = email.split('@')

            if len(parts) != 2 or '.' not in parts[0]:
                print(f'Skipping the line {row_number}: "{email}". Wrong format', file=sys.stderr)
                continue

            name_parts = parts[0].split('.')
            name = name_parts[0].capitalize()
            surname = name_parts[1].capitalize()
            employees.append([name, surname, email])

    return employees

def write_tsv(employees: list, filename: str) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        file.write('\t'.join(['Name', 'Surname', 'E-mail']) + '\n')
        for emp in employees:
            file.write('\t'.join(emp) + '\n')

if __name__ == "__main__":
    if len(sys.argv) == 3:
        input_file = sys.argv[1] #emails.txt
        output_file = sys.argv[2] #employees.tsv
        
        employees = get_emails(input_file)
        write_tsv(employees, output_file)


    
