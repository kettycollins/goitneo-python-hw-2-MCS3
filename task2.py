from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name.lower())

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False


class PhoneValidationError(Exception):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise PhoneValidationError("Phone should contain exactly 10 digits")
        super().__init__(value)


"""Тут не потрібен декоратор, класи мають тільки описувати структуру даних"""

# # декоратор для обробки помилок вводу
# def input_error(func):
#     def inner(*args, **kwargs):
#         try:
#             return func(*args, **kwargs)
#         except ValueError:
#             return "Give me name and phone please."
#         except KeyError:
#             return "Enter user name."
#         except IndexError:
#             return "Give me name and phone please."
#         except PhoneValidationError:
#             return "Phone number must be a 10-digit number"

#     return inner


class Record:
    def __init__(self, name):
        self.name = Name(name.lower())
        self.phones = []

    def add_phone(self, phone):
        # валідація нового номеру телефону
        try:
            phone_obj = Phone(phone)
        except PhoneValidationError as e:
            return str(e)

        self.phones.append(phone_obj)

    def remove_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                self.phones.remove(phone_obj)
                return

    def edit_phone(self, old_phone, new_phone):
        # валідація нового номеру телефону
        """try except тут лишній, метод просто має викинути помилку, якщо дані не валідні,
        а обробкою буде займатися викликаючий код"""
        # try:
        new_phone = Phone(new_phone)
        # except PhoneValidationError as e:
        #     return str(e)
        for idx, phone in enumerate(self.phones):
            if phone.value == old_phone:
                self.phones[idx] = new_phone # варто замінити весь екземпляр
                return
            
    def find_phone(self, phone):
        for phone_obj in self.phones:
            if phone_obj.value == phone:
                return phone_obj

    def __str__(self):
        phone_str = "; ".join(str(phone) for phone in self.phones)
        return f"Contact name: {self.name.value}, phones: {phone_str}"


def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
    
    # contacts = AddressBook()
    # print("Welcome to the assistant bot!")
    # while True:
    #     user_input = input("Enter a command: ")
    #     command, *args = user_input.split()
    #     command = command.strip().lower()
    #     if command in ["close", "exit"]:
    #         print("Good bye!")
    #         break
    #     elif command == "hello":
    #         print("How can I help you?")
    #     elif command == "add":
    #         if len(args) < 2:
    #             print("Give me name and phone please.")
    #             continue
    #         name, phone = args
    #         record = Record(name.lower())
    #         message = record.add_phone(phone)
    #         if message:
    #             print(message)
    #         else:
    #             contacts.add_record(record)
    #             print("Contact added.")
    #     elif command == "change":
    #         name, phone = args
    #         record = contacts.find(name.lower())
    #         if record:
    #             message = record.edit_phone(record.phones[0].value, phone)
    #             if message:
    #                 print(message)
    #             else:
    #                 print("Contact updated.")
    #         else:
    #             print("Contact not found.")
    #     elif command == "remove":
    #         name = args[0]
    #         if contacts.delete(name.lower()):
    #             print("Contact removed.")
    #         else:
    #             print("Contact not found.")
    #     elif command == "phone":
    #         name = args[0]
    #         record = contacts.find(name.lower())
    #         if record:
    #             if record.phones:
    #                 print(record.phones[0])
    #             else:
    #                 print("No phone number for this contact.")
    #         else:
    #             print("Contact not found.")
    #     elif command == "all":
    #         if not contacts.data:
    #             print("No contacts found.")
    #         else:
    #             for name, record in contacts.data.items():
    #                 if record.phones:
    #                     print(f"{name.capitalize()}: {record.phones[0]}")
    #                 else:
    #                     print(f"{name.capitalize()}: No phone number")
    #     else:
    #         print("Invalid command.")


if __name__ == "__main__":
    main()
