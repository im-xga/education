import re

num = input('Уведіть номер Вашої маршрутки:')
if num.isdigit():
    num_sequense = re.sub(r'(\d)(?=\d)', r'\1\n ', num)
    print("Ваша маршрутка:\n", num_sequense)
else:
    print("Тільки цифри!", num)