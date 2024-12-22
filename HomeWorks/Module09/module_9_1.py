# Домашнее задание по теме "Введение в функциональное программирование"

# Задача "Вызов разом":

# Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:
# int_list - список из чисел (int, float)
# *functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)
# Эта функция должна:
# Вызвать каждую функцию к переданному списку int_list
# Возвращать словарь, где ключом будет название вызванной функции,
# а значением - её результат работы со списком int_list.

# Пункты задачи:
# 1 В функции apply_all_func создайте пустой словарь results.
# 2 Переберите все функции из *functions.
# 3 При переборе функций записывайте в словарь results результат работы этой функции под ключом её названия.
# 4 Верните словарь results.
# 5 Запустите функцию apply_all_func, передав в неё список из чисел и набор других функций.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        # name = func.__name__
        # result = func(int_list)
        results.update({func.__name__: func(int_list)})
    return results

int_list = [12, 4, 75.67, -45, 8.846465849]

def min(int_list):  # - принимает список, возвращает минимальное значение из него.
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] < int_list[i + 1]:
            result = int_list[i]
    return result

def max(int_list):  # - принимает список, возвращает максимальное значение из него.
    i = 0
    for i in range(len(int_list)-1):
        if int_list[i] > int_list[i + 1]:
            result = int_list[i]
    return result

def len_(int_list):  # - принимает список, возвращает кол-во элементов в нём.
    result = len(int_list)
    return result

def sum(int_list):  # - принимает список, возвращает сумму его элементов.
    result = 0
    for i in int_list:
        result += i
    return result

def sorted_(int_list):  # - принимает список, возвращает новый отсортированный список на основе переданного.
    result = sorted(int_list)
    return result

def midle(int_list):  # - принимает список, возвращает среднее значение его элементов.
    result = 0
    for i in int_list:
        result += i
    result = result / len_(int_list)
    return result


print(apply_all_func(int_list, min, max, sum, midle))
print(apply_all_func(int_list, len_, sorted_))


# Примечания:
# Для того, чтобы взять название функции можно обратиться к атрибуту __name__
# При попытке передачи, например, списка из строк, некоторые функции могут работать некорректно или вовсе не работать.
# Используйте списки чисел.