# Дополнительное практическое задание по модулю: "Базовые структуры данных."  # ИСПРАВЛЕНО

# Задание "Средний балл":
# Вам необходимо решить задачу из реальной жизни:
# "школьные учителя устали подсчитывать вручную средний балл каждого ученика,
# поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students, где ключом будет имя ученика,
# а значением - его средний балл.

# __________________________Р_Е_Ш_Е_Н_И_Е:_______________________________________________ #
# Определим входные данные
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

averagescores = {}  # создадим пустой словарь (средних баллов)
# Упорядочим имена учеников из Множества students для создания ключей словаря
names = list(sorted(students))  # преобразуем множество в упорядоченный список
# names = list(students)  # преобразуем множество
# names.sort()            # в упорядоченный список
# Заполним словарь средними баллами учеников
averagescores.update({names[0]:sum(grades[0])/len(grades[0]), names[1]:sum(grades[1])/len(grades[1])})
averagescores.update({names[2]:sum(grades[2])/len(grades[2]), names[3]:sum(grades[3])/len(grades[3])})
averagescores.update({names[4]:sum(grades[4])/len(grades[4])})
print('Средние баллы учеников -', averagescores)    # Вывод в консоль