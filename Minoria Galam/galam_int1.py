import numpy as np
import matplotlib.pyplot as plt

# Definir los valores de a y L (numero de subgrupos)
a = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]
L = 6

#Definir probabilidad inicial a favor

Pyi = 0.70

def fact(j, k):
    if k < 0 or k > j:
        return 0
    return np.math.factorial(j) // (np.math.factorial(k) * np.math.factorial(j - k))

# Definir la función para calcular la sumatoria
def sumatoria(P, a, L):
    suma = 0
    for i in range(L):
        suma += a[i] * P[i]
    return suma

# Definir los valores iniciales de P
P = [0.7, 0, 0, 0, 0, 0]




def Prob(L, P0, *args): #Esta función es P(t+1), se calcula como aparece en el paper
    if np.sum(args) != 1 or len(args) != L: #Verifica que se cumplan lascondiciones del modelo
        return print('los valores de a_n no suman 1 o no coinciden con L') 
    else:
        total_sum = 0 #Se define para la suma total
        for i in range(1, len(args) + 1):
            a = args[i - 1]
            sum_i = 0 #Se define para la suma dentro de cada a_i
            for j in range(int(np.floor((i / 2) + 1)), i + 1):
                C =(np.math.factorial(i))/((np.math.factorial(i - j))*(np.math.factorial(j)))#Combinatoria
                Py = j #Probabilidad a favor
                Pn = i - j #Probabilidad en contra
                su = a * np.sum(C * P0 ** Py * (1-P0) ** Pn) 
                sum_i += su
                total_sum += su
        return sum_i, total_sum