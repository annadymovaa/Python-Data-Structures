import sys

def get_emails(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf-8') as file:
        emails = file.readlines()
    
    employees = list()
    for email in emails:
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

def write_tsv(employees: list):
    with open('employees.tsv', 'w', encoding='utf-8') as file:
        file.write('\t'.join(['Name', 'Surname', 'E-mail']) + '\n')
        for emp in employees:
            file.write('\t'.join(emp) + '\n')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        #emails.txt
        employees = get_emails(sys.argv[1])
        write_tsv(employees)


    
