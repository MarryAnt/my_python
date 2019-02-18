# cinema_price
film = input("Выберите фильм: ")
day = input("Выберите день(сегодня, завтра): ")
time = int(input("Выберите время: "))
num = int(input("Укажите количество билетов: "))
if film == "Пятница":
    if day == "сегодня":
        if time == 12:
            if num < 20:
                print("Заплатите ",250*num," рублей")
            elif num > 20:
                print("Заплатите ",250*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        elif time == 16:
            if num < 20:
                print("Заплатите ",350*num," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        elif time == 20:
            if num < 20:
                print("Заплатите ",450*num," рублей")
            elif num > 20:
                print("Заплатите ",450*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        else:
            print("Ошибка ввода")
    elif day == "завтра":
        if time == 12:
            if num < 20:
                print("Заплатите ",250*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",250*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        elif time == 16:
            if num < 20:
                print("Заплатите ",350*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        elif time == 20:
            if num < 20:
                print("Заплатите ",450*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",450*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        else:
            print("Ошибка ввода")
    else:
        print("Ошибка ввода")
elif film == "Чемпионы":
    if day == "сегодня":
        if time == 10:
            if num < 20:
                print("Заплатите ",250*num," рублей")
            elif num > 20:
                print("Заплатите ",250*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        elif time == 13:
            if num < 20:
                print("Заплатите ",350*num," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        elif time == 16:
            if num < 20:
                print("Заплатите ",350*num," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        else:
            print("Ошибка ввода")
    elif day == "завтра":
        if time == 10:
            if num < 20:
                print("Заплатите ",250*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",250*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        elif time == 13:
            if num < 20:
                print("Заплатите ",350*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        elif time == 16:
            if num < 20:
                print("Заплатите ",350*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        else:
            print("Ошибка ввода")
    else:
        print("Ошибка ввода")
elif film == "Пернатая банда":
    if day == "сегодня":
        if time == 10:
            if num < 20:
                print("Заплатите ",350*num," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        elif time == 14:
            if num < 20:
                print("Заплатите ",450*num," рублей")
            elif num > 20:
                print("Заплатите ",450*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        elif time == 18:
            if num < 20:
                print("Заплатите ",450*num," рублей")
            elif num > 20:
                print("Заплатите ",450*num*0.8," рублей")
            else:
                print("Ошибка ввода")
        else:
            print("Ошибка ввода")
    elif day == "завтра":
        if time == 10:
            if num < 20:
                print("Заплатите ",350*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",350*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        elif time == 14:
            if num < 20:
                print("Заплатите ",450*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",450*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        elif time == 18:
            if num < 20:
                print("Заплатите ",450*num*0.5," рублей")
            elif num > 20:
                print("Заплатите ",450*num*0.8*0.5," рублей")
            else:
                print("Ошибка ввода")
        else:
            print("Ошибка ввода")
    else:
        print("Ошибка ввода")
else:
    print("Ошибка ввода")
