# Модуль с классом User

class User:
    """Класс, представляющий пользователя"""

    def __init__(self, first_name, last_name):
        """Конструктор класса User"""
        self.first_name = first_name
        self.last_name = last_name

    def print_first_name(self):
        """Метод, печатающий имя"""
        print(self.first_name)

    def print_last_name(self):
        """Метод, печатающий фамилию"""
        print(self.last_name)

    def print_full_name(self):
        """Метод, печатающий имя и фамилию"""
        print(f'{self.first_name} {self.last_name}')
