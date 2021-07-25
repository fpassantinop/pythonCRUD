
import sys

clients = ['pablo','ricardo']

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients.append(client_name)
    else:
        print('Cliente already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print('{}:{}'.format(idx,client))


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
        client_name = _get_client_name()
        create_client(client_name)
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
