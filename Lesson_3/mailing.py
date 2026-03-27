# Модуль с классом Mailing

class Mailing:
    """Класс, представляющий почтовое отправление"""

    def __init__(self, to_address, from_address, cost, track):
        """Конструктор класса Mailing"""
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
