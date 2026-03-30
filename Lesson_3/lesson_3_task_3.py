# Урок 3, Задание 3
# Почтовое отправление

from address import Address
from mailing import Mailing

# Создаем адрес отправителя
from_address = Address(
    index='101000',
    city='Москва',
    street='Тверская',
    house='15',
    apartment='25'
)

# Создаем адрес получателя
to_address = Address(
    index='190000',
    city='Санкт-Петербург',
    street='Невский проспект',
    house='28',
    apartment='12'
)

# Создаем экземпляр класса Mailing
mailing = Mailing(
    to_address=to_address,
    from_address=from_address,
    cost=350.50,
    track='TRK123456789'
)

# Распечатываем отправление (разбиваем длинную строку)
print(
    f'Отправление {mailing.track} из {mailing.from_address.index}, '
    f'{mailing.from_address.city}, {mailing.from_address.street}, '
    f'{mailing.from_address.house} - {mailing.from_address.apartment} '
    f'в {mailing.to_address.index}, {mailing.to_address.city}, '
    f'{mailing.to_address.street}, {mailing.to_address.house} - '
    f'{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.'
)
