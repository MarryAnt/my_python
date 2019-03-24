lst = []
s = 0
with open('tempre.txt','r') as file:
    tempers = file.readlines()
for i in tempers:
    s += float(i)
    lst.append(float(i))
print('Максимальная температура: ',max(lst))
print('Минимальная температура: ',min(lst))
print('Среднее значение температуры: ',s/len(lst))
print('Количество уникальных температур в файле: ',len(set(lst)))
