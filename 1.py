import random

def pro(i, j):
    if i == j:
        return i
    return "Нет элементов"

a = int(input("Введите размерность массива A:"))
b = int(input("Введите размерность массива B:"))
A = random.sample(range(20), a)
B = random.sample(range(20), b)
for i in A:
    for j in B:
        print(pro(i,j))