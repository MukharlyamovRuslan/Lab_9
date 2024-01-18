from random import shuffle
import keyboard
import logging
n = []
# Настройка логгирования
logging.basicConfig(filename="Lab_9.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
# Ввод числа пользователем и проверка на ошибку
while True:
    try:
        number = int(input('Введите натуральное число N: '))
        logging.info(f"Логи для числа {number}")
        logging.info(f"Число введенное ползователем {number}")
        if number > 0:
            break
    except ValueError:
        print('Вы ввели что-то не то')
        logging.error("Ошибка ввода числа пользователем")
# Случайный порядок чисел
for i in range(1, number + 1):
    n.append(i)
shuffle(n)
print('')
# Нажатие кнопки
for el in n:
    print('Нажмите alt, чтобы вытащить бочонок')
    keyboard.wait('alt')
    print('Выпавшее число','-', el)
    logging.info(f"Числа сгенерированные программой {el}")
logging.info("")