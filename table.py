# table
elem = input("Введите номер элемента: ")
if elem:
    num = int(elem)
    if num == 3:
        print("Li")
    elif num == 25:
        print("Mn")
    elif num == 80:
        print("Hg")
    elif num == 17:
        print("Cl")
    else:
        print("Что это?")
else:
    print("Введите номер элемента!")
