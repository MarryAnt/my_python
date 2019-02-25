import random
num = int(input("Введите число от 1 до 4: "))
numPK = random.randint(1,4)
if num == numPK:
    print("Победа!")
elif num > numPK:
    print("Попробуйте еще раз! Загаданное число меньше Вашего!")
else:
    print("Попробуйте еще раз! Загаданное число больше Вашего!")
