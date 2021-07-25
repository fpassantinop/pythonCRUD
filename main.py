
import sys

clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer'
    },
     {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'pablo@facebook.com',
        'position': 'Data engineer'
    }
]

def create_client(client):
    global clients

    if client in clients:
        clients.append(client)
    else:
        print('Cliente already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))


def update_client_name(client_name, updated_client_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_client_name
    else:
        print('Client is not in client list')


def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        print('Client is not in client list')


def search_client(client_name):
    global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            return True


def _print_welcome():
    print("Welcome to Francis Ventas")
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')  
    print('[U]pdate cliente')  
    print('[D]reate cliente')  
    print('[S]earch cliente')  


def _get_client_field(field_name):
    field = None

    while not field:
        field = input('What is the client {}?'.format(field_name))


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the cliente name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()
    
    return client_name



if __name__ == '__main__':
    _print_welcome()
    comand = input()
    comand = comand.upper()


    if comand == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif comand == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif comand == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client_name(client_name,updated_client_name)
        list_clients()
    elif comand == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the clients list')
        else:
            print('the client: {} is not in our clients list'.format(client_name))
    else:
        print('Invalid command')
