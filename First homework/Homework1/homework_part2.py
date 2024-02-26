def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=2)
    cmd = parts[0].lower()
    args = parts[1:] if len(parts) > 1 else []
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Please provide a name and phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return "Please provide a name and a new phone number."
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def get_phone(args, contacts):
    if not args:
        return "Please provide a contact name."
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Contact not found."

def list_contacts(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            response = add_contact(args, contacts)
            print(response)
        elif command == "change":
            response = change_contact(args, contacts)
            print(response)
        elif command == "phone":
            response = get_phone(args, contacts)
            print(response)
        elif command == "all":
            response = list_contacts(contacts)
            print(response)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
