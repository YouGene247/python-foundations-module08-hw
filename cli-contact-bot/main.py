from typing import Callable

class InvalidPhoneError(Exception): pass
class InvalidNameError(Exception): pass


def input_error(func: Callable):

    def inner (*args, **kwargs):

        try:
            return func(*args, **kwargs)
         
        except (ValueError, IndexError):
            return "Missing argument. Use 'help' for correct command format."
        
        except NameError:
            return "Contacts are not created yet. Use 'add' to create one."

        except KeyError:
            return "Contact is missing. Use 'add' to create one."
        
        except InvalidNameError:
            return "Wrong name input format. Use 'help' for correct command format."
        
        except InvalidPhoneError:
            return "Wrong phone input format. Use 'help' for correct command format."


    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args

    if not name.isalpha():
        raise InvalidNameError
    
    if not (phone.isdigit() and len(phone) <= 10):
        raise InvalidPhoneError
    
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args

    if not name.isalpha():
        raise InvalidNameError
    
    if not (phone.isdigit() and len(phone) <= 10):
        raise InvalidPhoneError
    
    if name in contacts.keys():
        contacts[name] = phone
        return "Contact changed."
    else:
        contacts[name] = phone
        return f"{name} was missing, so it was created"

@input_error
def list_contacts(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"Name: {name}. Phone: {phone}")
    else:
        print("No contacts created yet. Use 'add' to create one")

@input_error
def get_phone_by_name(args, contacts):
    name = args[0]

    if not name.isalpha():
        raise InvalidNameError

    if name in contacts.keys():
        return f"Name: {name}. Phone: {contacts[name]}"
    else:
        raise KeyError
    

def help():
    
    use_cases = ['add contact', 'update contact', 'list all contacts', 'get phone by username', 'close/exit program']
    command_examples = ['add johndoe +3800000000', 'change johndoe +3800000000', 'all', 'phone johndoe', 'close|exit']
    
    col1_width = len(max(use_cases, key = len))
    col2_width = len(max(command_examples, key = len))
    
    table_header = f"|{'USE CASE'.center(col1_width,' ')}|{'COMMAND EXAMPLE'.center(col2_width,' ')}|"
    table_body = zip(use_cases,command_examples)

    print(table_header)
    print(''.center(len(table_header),"_"))

    for col1_value, col2_value in table_body:
        row = f"|{col1_value.center(col1_width,' ')}|{col2_value.center(col2_width,' ')}|"
        print(row)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Use 'help' to see the lists of supported commands")

    while True:
        try:
            user_input = input("Enter a command: ")

            if not user_input:
                continue

            command, *args = parse_input(user_input)

            match command:
                
                case "close" | "exit":
                    print("Good bye!")
                    break
                
                case "hello":
                    print("How can I help you?")

                case "help":
                    help()
                
                case "add":
                    print(add_contact(args, contacts))

                case "change":
                    print(change_contact(args, contacts))
                
                case "all":
                    list_contacts(contacts)
                    
                case "phone":
                    print(get_phone_by_name(args, contacts))
   
                case _:
                    print("Unknown command. Use 'help' to see the list of available commands.")

        except KeyboardInterrupt:
            print("Good bye!")
            break



if __name__ == "__main__":
    main()