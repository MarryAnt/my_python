from math import sqrt
lst1 = [2,4,9,16,25]
for i in range(len(lst1)):
    lst1[i] = sqrt(lst1[i])
print(lst1)
print(list(map((lambda x: sqrt(x)),[2,4,9,16,25])))
print([sqrt(i) for i in [2,4,9,16,25]])
