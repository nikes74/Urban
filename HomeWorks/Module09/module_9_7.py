# ИСПРАВЛЕНО # Домашнее задание по теме "Декораторы" # ИСПРАВЛЕНО #

# Задание:
# Напишите 2 функции:
# 1 Функция, которая складывает 3 числа (sum_three)
# 2 Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1-ой функции будет простым числом
#   и "Составное" в противном случае.

# Примечания:
# 1 Не забудьте написать внутреннюю функцию wrapper в is_prime
# 2 Функция is_prime должна возвращать wrapper
# 3 @is_prime - декоратор для функции sum_three

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
def is_prime(func):
    def wrapper(*args):
        n = func(*args)
        if n < 2:  # не 0 и не 1
            res = f'{n} - не простое и не сложное число'
        elif n == 2 or n == 3:
            res = f'{n} - Простое число'
        else:
            f = n ** (1 / 2)  # Корень квадратный из n
            for a in range(2, int(f) + 1):
                if n % a == 0:
                    res = f'{n} - Составное число'
                    break
                else:
                    res = f'{n} - Простое число'
        print(res)
        return n
    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    global saved_args   # для вывода значений аргументов функций в итоговую строку с результатом print(result)
    saved_args = {**locals()}
    # print(f'Cумма чисел {locals().get('a')}, {locals().get('b')} и {locals().get('c')}:') # а можно и в начале ;-)
    return a + b + c

result = sum_three(35, 8, 28) # 15, 8, 28
print(result, f'- cумма чисел {saved_args.get('a')}, {saved_args.get('b')} и {saved_args.get('c')}')