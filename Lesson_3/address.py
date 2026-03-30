# Модуль с классом Address

class Address:
    """Класс, представляющий почтовый адрес"""

    def __init__(self, index, city, street, house, apartment):
        """Конструктор класса Address"""
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
