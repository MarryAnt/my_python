import operator
lst = input('Введите последовательность: ').split()
st = []
actions = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
for i in lst:
    if i in actions:
        y, x = st.pop, st.pop()
        st.append(actions[i](x,y))
    elif i:
        st.append(int(i))
print(st.pop())
