# Домашнее задание по теме "Генераторы"

# Задача:
# Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

# Пункты задачи:
# 1 Напишите функцию-генератор all_variants(text).
# 2 Опишите логику работы внутри функции all_variants.
# 3 Вызовите функцию all_variants и выполните итерации.

# Примечания:
# Для функции генератора используйте оператор yield.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
import itertools # для Варианта 2

# Вариант 1
# Воспользуемся медодом "нарезки строк" для поиска всех подстрок переданной в функцию строки
def all_variants1(text):
  length = len(text)
  for x in range(length):
    for y in range(x,length):
      yield text[x:y + 1]
# Здесь подпоследовательности переданной строки выводятся перебором каждого символа строки в сочетании
# с последующей частью строки

# ВАРИАНТ 2
# Получим все возможные комбинации символов строки, воспользовавшись модулем itertools
def all_variants2(text):
    for i in range(len(text)):                        # len(text)-1 - для исключения полной строки
      combinations = []   # Создадим пустой список подпоследовательностей (комбинаций) для каждой итерации
      combinations = itertools.combinations(text, i + 1)  # +1 - для исключения пустой комбинации
      subsequences = [''.join(c) for c in combinations]   # Подготовим список для преобразования в строку
      declimer = f'\n'
      res = declimer.join(subsequences)          # Подготовим строку для вывода с построковой разбивкой по элементам
      yield res                                  # Сгенерируем строки
# Здесь подпоследовательности переданной строки выводятся по возрастанию
# количества комбинируемых между собой символов строки.
# Выводятся все комбинации между собой всех символов подстроки, исключая полную, она выводится как есть.

text1 = 'abc'
text2 = "abcd"

a = all_variants1(text1)
print(f'Строка "{text1}" имеет следующие комбинации символов:')
for i in a:
    print(i)

a = all_variants1(text2)
print(f'\nСтрока "{text2}" имеет следующие комбинации символов:')
for i in a:
  print(i)

b = all_variants2(text = text2) # 'abcd'
print(f'\nСтрока "{text2}" имеет следующие комбинации символов:')
for i in b:
    print(i)

b2 = all_variants2(text = text1) # 'abc'
print(f'\nСтрока "{text1}" имеет следующие комбинации символов:')
for i in b2:
    print(i)