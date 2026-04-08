import sys

def choose_task(task:str, valid_tasks: list):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if task == valid_tasks[0]:
        message = 'Contact these individuals via call center'
        ans = call_center(clients, recipients)
    elif task == valid_tasks[1]:
        message = 'Send these people an introductory email about our products'
        ans = potential_clients(participants, clients)
    elif task == valid_tasks[2]:
        message = 'Send these people a link to the event video and slides'
        ans = loyalty_program(participants, clients)

    print(f'{message}:\n{ans}')

def call_center(clients: list, recipients: list) -> list:
    clients = set(clients)
    recipients = set(recipients)
    not_seen = list(clients - recipients)
    return not_seen

def potential_clients(participants: list, clients: list) -> list:
    clients = set(clients)
    participants = set(participants)
    pot_cli = list(participants - clients)
    return pot_cli

def loyalty_program(participants: list, clients: list) -> list:
    clients = set(clients)
    participants = set(participants)
    send_link = list(clients - participants)
    return send_link

if __name__ == "__main__":
    if len(sys.argv) == 2:
        task = sys.argv[1]
        valid_tasks = ['call_center', 'potential_clients', 'loyalty_program']

        if task not in valid_tasks:
            raise Exception('Not a valid task!')
        else:
            choose_task(task, valid_tasks)
