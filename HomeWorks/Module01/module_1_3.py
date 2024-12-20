# Практическая работа по уроку "Динамическая типизация"

# Создайте переменные разных типов данных:
#   - Создайте переменную name и присвойте ей значение вашего имени (строка).
#   - Выведите значение переменной name на экран.
#   - Создайте переменную age и присвойте ей значение вашего возраста (целое число).
#   - Выведите значение переменной age на экран.
#   - Перезапишите в age текущее значение переменной age + новое.
#   - Выведите измененное значение переменной age на экран.
#   - Создайте переменную is_student и присвойте ей значение True (логическое значение).
#   - Выведите значение переменной is_student на экран.

# Примечания:
# - Для вывода значений на экран используйте функцию print().
# - Обратите внимание на использование разных типов данных и возможности их изменения.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
name = 'Alexey' # str
print(name)
age = 50    # int
print(age)
age = age + (366 - 42) / 366    # int --> float
print(age)
is_student = True   # bool
print(is_student)