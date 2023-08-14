import math
import matplotlib.pyplot as plt
import numpy as np

#Definimos una función para calcular el coeficiente binomial
def binom(k, j):

    return math.factorial(k) // (math.factorial(j) * math.factorial(k - j))

# Definimos ambas sumatorias
def calculo(L, a, Py):
    P_plus_t1 = 0
    
    for k in range(1, L + 1):
        sumatoria1 = 0
        for j in range(int((k//2)+1), k + 1):
            coef = binom(k,j)
            sumatoria1 += coef * (Py ** j) * ((1 - Py) ** (k - j))
        
        P_plus_t1 += a[k - 1] * sumatoria1
    return P_plus_t1 

#Condiciones iniciales
Py1 = np.linspace(0,1,100) #Valor inicial de Poblacion a favor
Py2 = np.linspace(0,1,100)

a1 = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1] # todos los valores de cada a_i
a2 = [0,0.1,0.9]
L1 = len(a1)   #Numero de grupos a_i
L2 = len(a2)


# Iterar para varios valores de t
iteraciones = 1
val_tm1_1 = [Py1]
val_tm1_2 = [Py2]
for i in range(iteraciones):
    tm1_1 = calculo(L1, a1, Py1)
    tm1_2 = calculo(L2,a2,Py2)
    val_tm1_1.append(tm1_1)
    val_tm1_2.append(tm1_2)
    Py1 = tm1_1
    Py2 = tm1_2




pt_1 = val_tm1_1[:-1] #Tomamos todos excepto el último
ptm1_1 = val_tm1_1[1:] # tomamos todos los valores excepto el primero

pt_2 = val_tm1_2[:-1]
ptm1_2 = val_tm1_2[1:]

# Crear el gráfico
plt.figure()

plt.plot(pt_1, ptm1_1, linestyle='-', color='blue', linewidth=10)
plt.plot(pt_2, ptm1_2, marker='x', linestyle='-', color='b',linewidth=1)
plt.plot([0, 1], [0, 1], linestyle='--', color='red')
plt.xlabel('P(t)')
plt.ylabel('P(t+1)')
plt.title('Gráfico de P(t) vs P(t+1)')
plt.grid('True')
plt.show()
