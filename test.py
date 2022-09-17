import re

num = input('Уведіть номер Вашої маршрутки:')
if num.isdigit():
    num_sequense = re.sub(r'(\n)(?=\n)', r'\2 ', num)
    print("Ваша маршрутка:", num_sequense)
else:
    print("Тільки цифри!", num)