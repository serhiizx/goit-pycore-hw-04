
contacts = {
    'Serhii': '0981040101'
}

def handle_help(args):
    print("""
Command list:
help   - Show this help
new    - Add new contact
search - Search a contact
change - Change a contact
all    - Show all contacts
exit   - Exit the program
close  - Close the program
""")

def add_contact(args):
    name, phone = args
    contacts[name] = phone
    print("Contact added.")

def change_contact(args):
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        print('Contact changed.')
    else:
        contacts.setdefault(name, phone)
        print("Contact created.")

def show_all(args):
    print("Show all contacts:")
    for name, phone in contacts.items():
        print(f"Name={name}, phone={phone}")

def handle_exit(args):
    print('Good bye!')
    exit(0)

commands = {
    'help': handle_help,
    'all': show_all,
    'add': add_contact,
    'change': change_contact,
    'exit': handle_exit,
    'close': handle_exit,
}

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the assistant bot!\nContact Manager 1.0.\nEnter 'help' to see all supported commands.")

    while True:
        user_input = input(">> ")
        command, *args = parse_input(user_input)

        if command in commands:
            commands[command](args)
        else:
            print(f"Invalid command. You should use one of these commands: {list(commands.keys())}")

if __name__ == "__main__":
    main()