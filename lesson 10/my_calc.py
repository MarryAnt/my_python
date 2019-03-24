try:
    num1 = int(input('Введите первое число: '))
    num2 = int(input('Введите второе число: '))
    oper = input('Введите опператор(add,sub,mul,div): ')
    if oper == 'add':
        print(num1+num2)
    elif oper == 'sub':
        print(num1-num2)
    elif oper == 'mul':
        print(num1*num2)
    elif oper == 'div':
        print(num1/num2)
    else:
        print('Компьютер не понимает, какое действие Вы хотите выполнить!')
except ZeroDivisionError:
    print('В ходе работы программы возникла ошибка деления на ноль!')
except ValueError:
    print('В ходе работы программы возникла ошибка преобразования типов!')
