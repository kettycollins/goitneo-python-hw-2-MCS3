# декоратор для обробки помилок вводу
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Give me name and phone please."

    return inner


# class PhoneValidationError(Exception):
#     pass


# # клас Phone з валідацією помилки на кількість цифр
# class Phone:
#     def __init__(self, value):
#         if not value.isdigit() or len(value) != 10:
#             raise PhoneValidationError("Phone should contain exactly 10 digits.")
#         self.value = value


# розбиває введений рядок на слова, використовуючи пробіл як розділювач
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


# новий контакт
@input_error
def add_contact(args, contacts):
    name = args[0]
    phone = args[1]
    # валідація номера телефону
    # try:
    #     phone = 
    # except PhoneValidationError as e:
    #     return str(e)
    contacts[name.lower()] = phone
    return "Contact added."


# змінити контакт
@input_error
def change_contact(args, contacts):
    name, phone = args
    # валідація номера телефону
    # try:
    #     phone = Phone(phone)
    # except PhoneValidationError as e:
    #     return str(e)
    contacts[name.lower()] = phone
    return "Contact updated."


# показати контакт
@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts[name.lower()]


# показати всі контакти
@input_error
def show_all(args, contacts):
    if not contacts:
        return "No contacts found."
    result = "\n".join(
        [f"{name.capitalize()}: {phone}" for name, phone in contacts.items()]
    )
    return result


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
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(args, contacts)
            print(result)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
