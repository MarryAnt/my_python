from pprint import pprint

dict_cinema = {
    'Пятница': {'time_price': {12: 250, 16: 350, 20: 450}, 'genre': 'комедия', 'limit': 16},
    'Чемпионы': {'time_price': {10: 250, 13: 350, 16: 350}, 'genre': 'спорт', 'limit': 16},
    'Пернатая банда': {'time_price': {10: 350, 14: 450, 18: 450}, 'genre': 'мультфильм', 'limit': 6}    
    }
film = input("Выберите фильм: ")
day = input("Выберите день(сегодня, завтра): ")
time = int(input("Выберите время: "))
num = int(input("Укажите количество билетов: "))
c = dict_cinema[film]['time_price'][time]
if day == "сегодня":
    if num < 20:
         print("Заплатите ",c*num," рублей")
    elif num > 20:
        print("Заплатите ",c*num*0.8," рублей")
    else:
        print("Ошибка ввода")
elif day == "завтра":
    if num < 20:
         print("Заплатите ",c*num*0.5," рублей")
    elif num > 20:
        print("Заплатите ",c*num*0.8*0.5," рублей")
    else:
        print("Ошибка ввода")
else:
    print("Ошибка ввода")
