import time
import numpy as np
import matplotlib.pyplot as plt

def fibRecursion(n):
    if(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        return (fibRecursion(n-1)+fibRecursion(n-2))

def fibDP(n):
    array = [1,1]

    for i in range(2, n):
        array.append(i)
        array[i] = array[i-1]+array[i-2]
    return array[n-1]

while True:
    try:
        n = int(input('Digite um valor: '))
        if (n < 0):
            raise ValueError(n)
    except ValueError as e:
        print("Valor inválido:",e)
    else:
        break
print('--------------Recursivo--------------')
start = time.perf_counter()
print(f'Fibonacci de {n} = {fibRecursion(n)}')
print('Tempo de execução com recursão = {:0.10f}'.format(time.perf_counter() - start))

print('---------Programação Dinâmica---------')
start = time.perf_counter()
print(f'Fibonacci de {n} = {fibDP(n)}')
print('Tempo de execução com DP = {:0.10f}'.format(time.perf_counter() - start))

arrayRecursive = []
arrayDP = []

qtd = 20

for i in range(1, qtd+11, 1):
    start = time.perf_counter()
    fibRecursion(i)
    end = time.perf_counter()
    arrayRecursive.append(end - start)

for i in range(1, qtd+11, 1):
    start = time.perf_counter()
    fibDP(i)
    end = time.perf_counter()
    arrayDP.append(end - start)

print('-------------------')
arrayRecursiveS = []
arrayDPS = []

for i in arrayRecursive:
    arrayRecursiveS.append(format(i, '.10f'))

for i in arrayDP:
    arrayDPS.append(format(i, '.10f'))

print(f'Recursive array:\n{arrayRecursiveS}\n')
print(f'DP array:\n{arrayDPS}\n')

fn = []
for i in range(1,qtd+11,1):
    fn.append(i)

plt.plot(fn, arrayRecursive, 'ro')
plt.plot(fn, arrayRecursive, color='blue')

plt.plot(fn, arrayDP, 'go')
plt.plot(fn, arrayDP, color='red')


plt.grid(True)
plt.xlabel('Número de Fibonacci')
plt.ylabel('Tempo')
plt.show()
