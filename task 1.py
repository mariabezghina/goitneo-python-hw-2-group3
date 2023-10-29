def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Invalid index. Please provide a valid index."

    return inner

contacts = {}

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def show_contacts(args, contacts):
    if not contacts:
        return "No contacts available."
    
    result = "Contacts:\n"
    for i, (name, phone) in enumerate(contacts.items(), start=1):
        result += f"{i}. {name}: {phone}\n"
    
    return result

@input_error
def remove_contact(args, contacts):
    index = int(args[0]) - 1
    name_to_remove = list(contacts.keys())[index]
    del contacts[name_to_remove]
    return f"Contact '{name_to_remove}' removed."



while True:
    command = input("Enter command (add/show/remove/exit): ").lower()

    if command == "exit":
        break

    try:
        if command == "add":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            result = add_contact((name, phone), contacts)
        elif command == "show":
            result = show_contacts((), contacts)
        elif command == "remove":
            index = input("Enter index to remove: ")
            result = remove_contact((index,), contacts)
        else:
            result = "Invalid command. Available commands: add, show, remove, exit."

        print(result)

    except Exception as e:
        print(f"An error occurred: {e}")
