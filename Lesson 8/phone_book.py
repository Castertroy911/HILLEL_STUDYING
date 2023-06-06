import json


class Interface:
    @staticmethod
    def _action_to_do() -> str:
        action = input(f'Hello! \nIf you want to add new subscriber to the phone book - enter "add". '
                       f'\nIf you want to edit already added subscriber - enter "edit".'
                       f'\nIf you want to delete the subscriber from the phone book - enter "delete".'
                       f'\nIf you want to stop program - enter "stop".\n')
        return action

    @staticmethod
    def _get_users_data() -> tuple:
        name = str(input(f'[Required field]\nPlease, enter the subscribers name --> '))
        second_name = str(input(f'[Optional field]\nPlease, enter the subscribers second name --> '))
        phone_number = str(input(f'[Required field]\nPlease, enter the subscribers phone number --> '))
        birth_date = str(input(f'[Optional field]\nPlease, enter the subscribers birth date --> '))
        return name, phone_number, second_name, birth_date


class PhoneBook(Interface):
    __AMBULANCE_NUMBER = 101
    __POLICE = 102
    __FIRE_STATION = 103

    def __init__(self):
        self.users_data = self._get_users_data()
        self.subscriber = Subscriber(*self.users_data)

    def start(self):
        action = self._action_to_do()
        action = action.lower()
        if action != 'add' and action != 'edit' and action != 'delete':
            raise Exception(f'Entered action is not supported! Rerun program and try again. '
                            f'Valid arguments: "add", "edit", "delete"!')
        elif action == 'add':
            self.add_subscriber(*self.users_data)
        elif action == 'edit':
            self.edit_subscriber(*self.users_data)
        else:
            self.delete_subscriber(*self.users_data)

    def add_subscriber(self, name: str, phone_number: int, birth_date: int = None, second_name: str = None):
        if self.subscriber.is_phone_number():
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
        raise Exception('Phone number should start with "+"')


if __name__ == '__main__':
    a = PhoneBook()
    a.start()
    print(a.subscriber.data)
