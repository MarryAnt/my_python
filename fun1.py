# fun1
data = input("")
if data:
    num = float(data)
    if -2.4 <= num <= 5.7:
        print("Значение функции равно ",num**2)
    else:
        print("Значение функции равно 4")
else:
    print("Введите значение!")
