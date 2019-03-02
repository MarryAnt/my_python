import random
l = ['самовар','весна','лето']
n = random.randint(0,len(l)-1)
i = random.randint(0,len(l[n])-1)
x = list(l[n])
m = x[i]
del x[i:i+1]
x.insert(i,'?')
print(''.join(x))
s = input('Введите букву: ')
if s == m:
    print('Победа!\nCлово: ',l[n])
else:
    print('Увы, попробуйте в другой раз!\nCлово: ',l[n])
