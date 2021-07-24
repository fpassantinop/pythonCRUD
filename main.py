
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

def _add_comma():
    global clients

    clients += ','

def _print_welcome():
    print("Welcome to Francis Ventas")
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate cliente')  
    print('[D]reate cliente')  

if __name__ == '__main__':
    _print_welcome()
    comand = input()

    if comand == 'C':
        client_name = input('What is the cliente name? ')
        create_client(client_name)
        list_clients()
    elif comand == 'D':
        pass
    else:
        print('Invalid command')
