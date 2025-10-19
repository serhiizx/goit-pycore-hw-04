
contacts = {}

def handle_help(args):
    return """
Command list:
help   - Show this help
add    - Add new contact. Example: add username +0981112233
phone  - Show phone by contact. Example: phone username
change - Change contact phone. Example: change username +0982223344
all    - Show all contacts
exit   - Exit the program
close  - Close the program
hello  - Welcome message 
"""

def add_contact(args):
    if not len(args) == 2:
        return "Error: Command 'add' example: add username phone"

    name, phone = args

    if name in contacts:
        return "Can't add. Username exists. Please, use command 'change' to set new phone."

    contacts[name] = phone

    return "Contact added."

def change_contact(args):
    if not len(args) == 2:
        return "Error: Command 'change' example: change username phone"

    name, phone = args

    if name not in contacts:
        return f"Can't change. Contact '{name}' doesn't exists."

    contacts[name] = phone

    return "Contact changed."

def show_all(args):
    result = []
    for name, phone in contacts.items():
        result.append(f"Name={name}, phone={phone}")
    return '\n'.join(result)

def handle_exit(args):
    print('Good bye!')
    exit(0)

def find_by_phone(args):
    if not len(args) == 1:
        return "Error: Command 'phone' example: phone username"

    name = args[0]


    for contact_name, contact_phone in contacts.items():
        if contact_name.find(name) >= 0:
            return contact_phone

    return 'Contact is not found.'

def welcomme(args):
    return 'How can I help you?'

commands = {
    'help': handle_help,
    'add': add_contact,
    'phone': find_by_phone,
    'change': change_contact,
    'all': show_all,
    'exit': handle_exit,
    'close': handle_exit,
    'hello': welcomme
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
            print(commands[command](args))
        else:
            print(f"Invalid command. Type 'help' to see all supported commands.")

if __name__ == "__main__":
    main()