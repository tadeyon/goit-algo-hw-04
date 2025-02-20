def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError:
        return "Enter contact name and phone number."


def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return "Contact phone number has been changed."
        return "Contact doesn\'t exist! Use command 'add' instead."
    except ValueError:
        return "Enter contact name and phone number."

def contact_phone_number(name, contacts):
    if name in contacts:
        return contacts[name]
    return "Contact doesn\'t exist!"

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            try:
                command, name = parse_input(user_input)
                print(contact_phone_number(name, contacts))
            except ValueError:
                print("Enter contact name.")
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
