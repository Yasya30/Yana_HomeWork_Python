# Урок 3, Задание 2
# Каталог смартфонов

from smartphone import Smartphone

# Создаем пустой каталог
catalog = []

# Наполняем каталог 5 разными экземплярами
catalog.append(Smartphone('Apple', 'iPhone 15 Pro', '+79123456789'))
catalog.append(Smartphone('Samsung', 'Galaxy S24 Ultra', '+79234567890'))
catalog.append(Smartphone('Xiaomi', 'Redmi Note 13', '+79345678901'))
catalog.append(Smartphone('Google', 'Pixel 8 Pro', '+79456789012'))
catalog.append(Smartphone('Honor', 'Magic 6 Pro', '+79567890123'))

# Печатаем каталог
print('Каталог смартфонов:')
print('=' * 50)
for phone in catalog:
    print(f'{phone.brand} - {phone.model}. {phone.phone_number}')
