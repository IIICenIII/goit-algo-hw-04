def parse_input(user_input):
    cmd,*args=user_input.split()
    cmd=cmd.strip().casefold()
    return cmd,*args

def add_contact(args,contacts):
    name,number=args
    if name in contacts:
        return 'The number already exists.'
    else:
        contacts[name]=number
        return 'Contact added.'

def change_contact(args,contacts):
    name,number=args
    if name not in contacts:
        return 'There is no such contact.'
    contacts[name]=number
    return 'Contact updated.'

def show_phone(args,contacts):
    if args[0] not in contacts:
        return 'There is no such contact.'
    return contacts[args[0]]

def show_all(contacts):
    if len(contacts)==0:
        return 'The contact list is empty.'
    outlines=''
    for key,value in contacts.items():
        outlines+=f'{key}{' '*(10-len(key))}{value}\n'
    return outlines[:-1]


def main():
    print('Welcome to the assistant bot!')
    contacts={}
    while True:
        user_input=input('Enter a comand here please: ')
        cmd,*args=parse_input(user_input)
        
        if cmd in ['exit','close']:
            print('Good bye')
            break
        elif cmd=='hello':
            print('How can I help you?')
        elif cmd=='add':
            print(add_contact(args,contacts))
        elif cmd=='change':
            print(change_contact(args,contacts))
        elif cmd=='all':
            print(show_all(contacts))
        elif cmd=='phone':
            print(show_phone(args,contacts))
        else:
            print('Invalid command')



if __name__=='__main__':
    main()