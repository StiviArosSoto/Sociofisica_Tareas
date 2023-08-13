import math
import matplotlib.pyplot as plt


def coeficiente_binomial(j, k):
    if k < 0 or k > j:
        return 0
    return math.factorial(j) // (math.factorial(k) * math.factorial(j - k))


# =============================================================================
# def calculo(L, a, P_plus_t):
#     P_minus = 1 - P_plus_t
#     P_plus_t1 = 0
#     
#     # Valores de P(t) y P(t+1)
#     p_t_values = []
#     p_tmas1_values = []
#     
#     for k in range(1, L + 1):
#         sumatoria1 = 0
#         
#         for j in range(int((k//2)+1), k + 1):
#             coef_binomial = math.comb(j, k)
#             sumatoria1 += coef_binomial * (P_plus_t ** j) * (P_minus ** (k - j))
#         p_t_values.append(P_plus_t)    
#         P_plus_t1 += a[k - 1] * sumatoria1
#         P_plus_t = P_plus_t1
#         p_tmas1_values.append(P_plus_t1)
#     return P_plus_t1 , p_t_values, p_tmas1_values
# 
# =============================================================================
# Valores iniciales
t = 0
L = 6
a = [0.2, 0.2, 0.2, 0.2, 0.1, 0.1]


def calculo(L, a, Py):
    P_plus_t1 = 0
    
    # Valores de P(t) y P(t+1)
    p_t_values = []
    p_tmas1_values = []
    
    for k in range(1, L + 1):
        
        P_plus_t1 = 0
        sumatoria1 = 0
        #print(f'iteracion {k}')
        for j in range(int((k//2)+1), k + 1):
            coef_binomial = math.comb(j, k)
            sumatoria1 += coef_binomial * (Py ** j) * ((1 - Py) ** (k - j))
        
        p_t_values.append(Py) 
        print(f' iteracion {j} , p(t) es: {p_t_values[j-1]}')
        #print(f'valor de a = {a[k-1]}')
        P_plus_t1 += a[k - 1] * sumatoria1
        Py = P_plus_t1
        p_tmas1_values.append(P_plus_t1)
        #print(f' iteracion {j} , p(t+1) es: {P_plus_t1}')
    return P_plus_t1 , p_t_values, p_tmas1_values

# Valores de P(t) y P(t+1)
# =============================================================================
# p_t_values = []
# p_tmas1_values = []
# =============================================================================
Py = 0.7
# =============================================================================
# for k in range(1, L + 1):
#     
#     P_plus_t1 = 0
#     sumatoria1 = 0
#     #print(f'iteracion {k}')
#     for j in range(int((k//2)+1), k + 1):
#         coef_binomial = math.comb(j, k)
#         sumatoria1 += coef_binomial * (Py ** j) * ((1 - Py) ** (k - j))
#     
#     p_t_values.append(Py) 
#     print(f' iteracion {j} , p(t) es: {p_t_values[j-1]}')
#     #print(f'valor de a = {a[k-1]}')
#     P_plus_t1 += a[k - 1] * sumatoria1
#     Py = P_plus_t1
#     p_tmas1_values.append(P_plus_t1)
#     #print(f' iteracion {j} , p(t+1) es: {P_plus_t1}')
# =============================================================================


# =============================================================================
# # Iterar para varios valores de t
# for _ in range(100):  # Puedes ajustar la cantidad de iteraciones
#     p_t_values.append(P_plus_t)
#     P_plus_t1 = calcular_P_plus(L, a, P_plus_t)
#     p_tmas1_values.append(P_plus_t1)
#     P_plus_t = P_plus_t1
# =============================================================================


# =============================================================================
# pt = p_t_values
# ptm1 = p_tmas1_values
# =============================================================================
cal = calculo(L, a, Py)
pt , ptm1 = cal[1],cal[2]



#pt , ptm1 = calculo(L, a, P_plus_t)[1], calculo(L, a, P_plus_t)[2]
# Crear el gráfico
plt.figure()
plt.plot(pt, ptm1, marker='o', linestyle='-', color='b')
plt.plot([0, 1], [0, 1], linestyle='--', color='gray')
plt.xlabel('P(t)')
plt.ylabel('P(t+1)')
plt.title('Gráfico de P(t) vs P(t+1)')
plt.grid()
plt.show()
