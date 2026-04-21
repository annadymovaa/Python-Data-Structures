import sys

def find_name(email: str) -> str:
    with open('employees.tsv', 'r', encoding='utf-8') as file:
        for line in file:
        
            person = line.strip().split('\t')
            if email == person[2]:
                name = person[0]
                break
        return name

def print_letter(name: str) -> None:
    if name:
        print(f'Dear {name}, welcome to our team! We are sure that it will be a pleasure to work with you. \nThat’s a precondition for the professionals that our company hires.')
    else:
        print('Name not found')

if __name__ == "__main__":
    if len(sys.argv) == 2:
        name = find_name(sys.argv[1])
        print_letter(name)