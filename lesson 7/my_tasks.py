from pprint import pprint
D = dict()
while True:
    n = int(input('Укажите число: '))
    if n == 3:
        print("Выход из программы! До встречи!")
        break
    elif n == 1:
        t = input("Сформулирйте задачу: ")
        c = input("Добавьте категорию к задаче: ")
        ti = input("Добавьте время к задаче: ")
        D['task'] = t
        D['category'] = c
        D['time'] = ti
        print('Простой todo:\n1. Добавить задачу\n2. Вывести список задач\n3. Выход')
    elif n == 2:
        pprint(D)
        print('Простой todo:\n1. Добавить задачу\n2. Вывести список задач\n3. Выход')
    else:
        print("Что Вы хотите?")
        print('Простой todo:\n1. Добавить задачу\n2. Вывести список задач\n3. Выход')
