import sys

def get_emails(filepath: str) -> list:
    employees = list()
    with open(filepath, 'r', encoding='utf-8') as file:

        for email in file:
            email = email.strip()
            parts = email.split('@')
            name_parts = parts[0].split('.')
            if len(name_parts) >= 2:
                name = name_parts[0].capitalize()
                surname = name_parts[1].capitalize()
                employees.append([name, surname, email])
            else:
                raise IndexError('The provided email is of an incorrect structure!')
    return employees

def write_tsv(employees: list, filename:  str) -> None:
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


    
