# call_tell
key = int(input("Введите код города: "))
duration = int(input("Введите длительность разговора: "))
if key:
    if duration:
        if key == 343:
            print("Заплатите ",duration*15," рублей")
        elif key == 381:
            print("Заплатите ",duration*18," рублей")
        elif key == 473:
            print("Заплатите ",duration*13," рублей")
        elif key == 485:
            print("Заплатите ",duration*11," рублей")
        else:
            print("Извините, Вашего города нет в базе")
    else:
        print("Введите длительность разговора!")
else:
    print("Введите код города!")
