# ИСПРАВЛЕНО # Домашнее задание по теме "Генераторы"

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

# Воспользуемся медодом "нарезки строк" для поиска всех подстрок переданной в функцию строки
def all_variants(text):
  count = len(text)
  for x in range(count):
    for y in range(count):
      yield text[y: x + y + 1]
    count -= 1
# Здесь подпоследовательности переданной строки выводятся перебором каждого символа строки в сочетании
# с последующей частью строки

text1 = 'abc'
text2 = "abcd"

a = all_variants(text1)
print(f'Строка "{text1}" имеет следующие подпоследовательности:')
for i in a:
    print(i)

a = all_variants(text2)
print(f'\nСтрока "{text2}" имеет следующие подпоследовательности:')
for i in a:
  print(i)