
clients = 'pablo, ricardo, '

def create_client(client_name):
    global clients

    if client_name not in clients:
        clients  += client_name
        _add_comma() 
    else:
        print('Cliente already is in the client\'s list')


def list_clients():
    global clients

    print(clients)


def update_client_name(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ',', updated_client_name + ',')
    else:
        print('Client is not in client list')


def _add_comma():
    global clients

    clients += ','

def _print_welcome():
    print("Welcome to Francis Ventas")
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')  
    print('[U]pdate cliente')  
    print('[D]reate cliente')  


def _get_client_name():
    return input('What is the cliente name? ')



if __name__ == '__main__':
    _print_welcome()
    comand = input()
    comand = comand.upper()


    if comand == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif comand == 'D':
        pass
    elif comand == 'U':
        client_name = _get_client_name()
        updated_client_name = input('What is the updated client name? ')
        update_client_name(client_name,updated_client_name)
        list_clients()
    else:
        print('Invalid command')
