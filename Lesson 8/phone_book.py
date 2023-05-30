import json


class Interface:
    @staticmethod
    def _action_to_do() -> str:
        action = input(f'Hello! \nIf you want to add new subscriber to the phone book - enter "add". '
                       f'\nIf you want to edit already added subscriber - enter "edit".'
                       f'\nIf you want to delete the subscriber from the phone book - enter "delete".\n')
        return action

    @staticmethod
    def _get_users_data() -> tuple:
        name = input(f'[Required field]\nPlease, enter the subscribers name --> ')
        second_name = input(f'[Optional field]\nPlease, enter the subscribers second name --> ')
        phone_number = input(f'[Required field]\nPlease, enter the subscribers phone number --> ')
        birth_date = input(f'[Optional field]\nPlease, enter the subscribers birth date --> ')
        return name, phone_number, second_name, birth_date


class PhoneBook(Interface):
    __AMBULANCE_NUMBER = 101
    __POLICE = 102
    __FIRE_STATION = 103

    def __init__(self):
        self.action = self._action_to_do()
        self.users_data = self._get_users_data()
        self.subscriber = Subscriber(*self.users_data)

    def start(self):
        self.action.lower()
        if self.action != 'add' and self.action != 'edit' and self.action != 'delete':
            raise Exception(f'Entered action is not supported! Rerun program and try again. '
                            f'Valid arguments: "add", "edit", "delete"!')
        elif self.action == 'add':
            self.add_subscriber(*self.users_data)
        elif self.action == 'edit':
            self.edit_subscriber(*self.users_data)
        else:
            self.delete_subscriber(*self.users_data)

    def add_subscriber(self, name: str, phone_number: int, birth_date: int = None, second_name: str = None):
        if self.subscriber.is_phone_number() and self.subscriber.is_name() and self.subscriber.is_second_name() and self.subscriber.is_birth_date():
            self.subscriber.data[phone_number] = [name, second_name, birth_date]

    def edit_subscriber(self, name: str, phone_number: int, birth_date: int = None, second_name: str = None):
        if self.subscriber.data.get(phone_number) is not None:
            self.subscriber.data[phone_number] = [name, second_name, birth_date]


    def delete_subscriber(self, name: str, phone_number: int, birth_date: int = None, second_name: str = None):
        if self.subscriber.data.get(phone_number) is not None:
            del self.subscriber.data[phone_number]
            with open('phone book.json', 'a+') as file:
                json.dump(self.subscriber.data, file, indent=4)


class Subscriber:
    data = {}

    def __init__(self, name: str, phone_number: int, second_name: str = None, birth_date: str = None):
        self.__name = name
        self.__phone_number = phone_number
        self.__birth_date = birth_date
        self.__second_name = second_name

    def is_phone_number(self):
        if isinstance(self.__phone_number, str) and '+' in self.__phone_number:
            return True
        return False

    def is_name(self):
        if isinstance(self.__name, str):
            return True
        return False

    def is_birth_date(self):
        if isinstance(self.__birth_date, str) or self.__birth_date is None:
            return True
        return False

    def is_second_name(self):
        if isinstance(self.__second_name, str) or self.__birth_date is None:
            return True
        return False


if __name__ == '__main__':
    a = PhoneBook()
    a.start()
    a.subscriber.data
