# Домашнее задание по теме "Потоки на классах"

# Задача "За честь и отвагу!"

# Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
# Атрибут name - имя рыцаря. (str)
# Атрибут power - сила рыцаря. (int)
# А также метод run, в котором рыцарь будет сражаться с врагами:
# При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
# Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
# В процессе сражения количество врагов уменьшается на power текущего рыцаря.
# По прошествию 1 дня сражения (1 секунды) выводится строка
# "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
# Как можно заметить нужно сделать задержку в 1 секунду, инструменты для задержки выберите сами.

# Пункты задачи:
# 1 Создайте класс Knight с соответствующими описанию свойствами.
# 2 Создайте и запустите 2 потока на основе класса Knight.
# 3 Выведите на экран строку об окончании битв.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #

# Импорт необходимых модулей и функций
from time import sleep
from threading import Thread

class Knight(Thread):
    def __init__(self, name_, power):
        self.name_ = str(name_)     # имя рыцаря. (str)
        self.power = int(power)     # сила рыцаря. (int)
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали!')
        num_days = 0
        enemyes = 100
        while enemyes > 0: # >= self.power:
            sleep(1)    # задержка в 1 секунду
            num_days += 1   # количество дней сражения
            enemyes = enemyes - self.power
            if enemyes < 0:
                enemyes = 0
            print(f'{self.name_} сражается {num_days}-й день..., осталось {enemyes} воинов.')

        print(f'{self.name_} одержал победу спустя {num_days} дней(дня)!')

threads = []

knight1 = Knight('Lancelot', 6)
knight1.start()
knight2 = Knight('Arthur', 12)
knight2.start()

threads.append(knight1)
threads.append(knight2)

for thread in threads:
    thread.join()
print(f'\nВсе враги повержены, битвы закончены!')