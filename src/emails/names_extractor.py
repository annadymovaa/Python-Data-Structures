import sys

def get_emails(filepath: str) -> list:
    with open(filepath, 'r', encoding='utf-8')as file:
        emails = file.readlines()
    
    employees = [['Name', 'Surname', 'E-mail']]
    for email in emails:
        email = email.replace('\n', '')
        info = email.split('@')
        person = info[0].split('.')
        name = person[0].capitalize()
        surname = person[1].capitalize()
        employees.append([name, surname, email])
    return employees

def write_tsv(employees: list):
    with open('employees.tsv', 'w', encoding='utf-8') as file:
        for emp in employees:
            file.write('\t'.join(emp) + '\n')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        #emails.txt
        employees = get_emails(sys.argv[1])
        write_tsv(employees)


    
