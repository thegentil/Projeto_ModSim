# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 16:18:24 2015

@author: Nicolas Gentil e Nicolas Fonteyne

Projeto final - Pêndulo de Newton

Mod. Sim. - 1B

Pergunta: Quanto tempo é necessário para que o pêndulo pare, em função do ângulo em que a bolinha é solta?

Considerações Gerais:

- O fio que segura a bolinha não tem massa.
- A bolinha só se desloca nos eixos x e y do plano cartesiano.
- A bolinha é considerada como um ponto no espaço, este ponto é seu centro de massa.
- Temperatura do ar é constante em 25˚C

"""

# Importando as bibliotecas necessárias:

from Parametros import *

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace

'''
Iteração 1

Considerações Especificas:

- O pêndulo é constituido por apenas uma bolinha.
- Consideramos que a bolinha é de Chumbo

'''

#======================================================================================================================#

# FAZENDO OS CÁLCULOS:

    # FUNÇÃO DA DERIVADA:

def chumbo(v,t):
    dydt = v[1]
    dzdt = ((mChumbo*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mChumbo*l)
    return [dydt, dzdt]


    # DEFININDO OS PARÂMETROS A SEREM UTILIZADOS NO CÁLCULO:

Tinicial = 0    # Tempo inicial
Tfinal = 50000    # Tempo final
Nmed = (Tfinal*10)+1  # Número de medições no intervalo de tempo

TPM = Tfinal/Nmed     # Tempo por medição (s)

T = linspace(Tinicial, Tfinal, Nmed)  # criando a lista de tempo e o número de medições nesse intervalo de tempo

    # CRIANDO A LITSA DE ÂNGULOS PARA O GRÁFICO

Agrafico = []
for i in range(19):
    a = -90 + i*5
    Agrafico.append(a)


    # CALCULANDO OS VALORES DO EIXO Y DO GRÁFICO (TEMPO DE ESTABILIZAÇÃO)

Vgrafico = []
for i in range(19):

    print(i)
    print('')

    y0 = (math.pi/2) + (i*((math.pi/180)*5))
    z0 = 0
    V0 = [y0, z0]

    Z = odeint(chumbo, V0, T)

    for e in Z:
        e[0] = pi_rad(e[0])
        e[0] = e[0] - 180

    Tstop = []

    for x in range(1, len(Z)-1):

        if Z[x][0] > Z[x+1][0]:
            if Z[x][0] > Z[x-1][0]:
                if Z[x][0] <= 2:
                    Tstop.append(x*TPM)

    Vgrafico.append(Tstop[0])


#======================================================================================================================#

# PLOTANDO OS DADOS:

plt.plot(Agrafico, Vgrafico,'g')     # Definindo quais variaveis serão plotados
plt.axis([-90, 0, 0, max(Vgrafico)])     # Definindo os valores máx e min a serem plotados
plt.ylabel('Tempo(s)')     # Definindo a label do eixo y
plt.xlabel('Ângulo (graus)')     # Definindo a label do eixo x
plt.title('Chumbo')     # Definindo o título
plt.show()     # Faz o gráfico aparecer
