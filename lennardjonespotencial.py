import matplotlib.pyplot as plt
import numpy as np
#Variáveis
epsilon = eval(input(' ε em Kcal/mol: '))
sigma = eval(input('σ em Angstrom: '))
x =  2**(1/6)*sigma
r = np.linspace(0.00001,x+5,num=1000) #Vetor ligando o centro dos átomos sendo
Pot_LJ = 4*epsilon* ((sigma/r)**12 - (sigma/r)**6)#Fórmula para o potencial


#Plot do Gráfico
plt.figure(figsize=[8,5])
plt.plot(r,Pot_LJ,'r-',linewidth=1,label="$Pot$")
plt.rc('text', usetex=True)
plt.rc('xtick', labelsize=30)
plt.rc('ytick', labelsize=30)
plt.title("$Potencial\ de\ Lennard-Jones$",fontsize=30)
plt.xlim([0,15])
plt.ylim([-2,2])
plt.ylabel("$Energia\ Potencial(V)$",fontsize=15)
plt.xlabel("$Distância(A)$",fontsize=15)
plt.legend(frameon=False,fontsize=15)
plt.axhline(0, color='grey',linestyle='--',linewidth=2)
plt.axhline(-epsilon, color='grey', linestyle='--', linewidth=2)
plt.show()
