# Modelo de Ising con dinamica de Glauber
# 06-Junio-2023
#===================================================================
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
#-------------------------------------------------------------------
print('**INICIO**')
print('==========')
# Inicio contador temporal del programa
tini = datetime.now()
#-------------------------------------------------------------------
# Condiciones iniciales
N=10
steps = 300
beta = 1
curr_state = np.random.choice(np.array([-1,1]),size=(N,N))
#-----------------------------------------------
# Configuracion Figura
fig, (ax1, ax2, ax3) = plt.subplots(nrows = 1, ncols = 3, figsize = (15, 5))

# Figura Estado Inicial
ax1.matshow(curr_state, cmap = plt.cm.plasma)
ax1.set_xticks([])
ax1.set_yticks([])
ax1.set_title("Configuracion Inicial")
#-----------------------------------------------
# Dinamica
M = np.zeros(steps)
for i in range(steps):
   M[i] = np.sum(curr_state)

   # Evaluacion por espin
   for n in range(N**2):
      # elige un espin en la posicion (i,j) aleatoriamente
      i, j = np.random.randint(N), np.random.randint(N)
      votante = curr_state[i,j]
      #vecinos
      #vecino = np.array([(i+1, j), (i-1, j), (i, j+1), (i, j-1)])
      vecino = np.array([curr_state[(i-1)%N, j], curr_state[(i+1)%N, j], curr_state[i, (j-1)%N], curr_state[i, (j+1)%N]])
      indice_vecino = np.random.choice(len(vecino))
      vecino_seleccionado = vecino[indice_vecino]
      
      #comparar vecino y reemplazar
      if votante != vecino_seleccionado:
          #votante = vecino_seleccionado
          votante = -1*curr_state[i, j]
      else:
          votante = curr_state[i, j]
     #actualizar estado de los votantes
      curr_state[i, j] = votante          
          

#PYSLP INSTALAR-----------------------------------------------
# Figura Estado Final
ax2.matshow(curr_state, cmap = plt.cm.plasma)
ax2.set_xticks([])
ax2.set_yticks([])
ax2.set_title("Configuracion Final")
#-----------------------------------------------
# Figura Magnetizacion
ax3.plot(M/N**2,'-b')
ax3.set_xlabel("Step")
ax3.set_ylabel("Magnetizacion")
ax3.set_title("Magnetizacion vs tiempo")
ax3.grid(True)
#-----------------------
plt.show()
#===============================================================================================
# Fin contador temporal del programa
tfin = datetime.now()
dtie = tfin - tini
print('Tiempo ocupado (h:m:s:ns):', dtie)
#-----------------------------------------------
print('========')
print('**FIN**')