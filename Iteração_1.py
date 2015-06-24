# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 13:51:26 2015

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

y0 = math.pi/2
z0 = -1
V0 = [y0, z0]

Tinicial = 0    # Tempo inicial
Tfinal = 50000   # Tempo final
Nmed = (Tfinal*10)+1  # Número de medições no intervalo de tempo

TPM = Tfinal/Nmed     # Tempo por medição (s)

T = linspace(Tinicial, Tfinal, Nmed)  # criando a lista de tempo e o número de medições nesse intervalo de tempo


    # EXECUTANDO O CÁLCULO:

Z = odeint(chumbo, V0, T)       # obtendo os valores a serem plotados a parte da função da derivada da curva


    # TRANSFORMANDO OS DADOS DE RAD PARA GRAUS E ACERTANDO O MÓDULO:

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180


    # OBTENDO OS PONTOS MÁXIMOS DA FUNÇÃO ANTERIOR:

p_maximo = []
T2 = []


for i in range(1, len(Z)-1):

    if Z[i][0] > Z[i+1][0]:
        if Z[i][0] > Z[i-1][0]:
            p_maximo.append(Z[i][0])
            T2.append(i*TPM)


    # OBTENDO OS PONTOS MÍNIMOS DA FUNÇÃO ANTERIOR:

p_minimo = []
T3 = []

for i in range(1, len(Z)-1):

    if Z[i][0] < Z[i+1][0]:
        if Z[i][0] < Z[i-1][0]:
            p_minimo.append(Z[i][0])
            T3.append(i*TPM)

#======================================================================================================================#

# PLOTANDO OS DADOS:

plt.plot(T, Z[:, 0],'g')     # Definindo quais variaveis serão plotados
plt.axis([0, max(T), -100, 100])     # Definindo os valores máx e min a serem plotados
plt.ylabel('Ângulo (graus)')     # Definindo a label do eixo y
plt.xlabel('Tempo (s)')     # Definindo a label do eixo x
plt.title('Chumbo')     # Definindo o título
plt.show()     # Faz o gráfico aparecer

plt.plot(T2, p_maximo, 'r')     # Definindo quais variaveis serão plotados
plt.plot(T3, p_minimo, 'b')     # Definindo quais variaveis serão plotados
plt.axis([0, max(T2), -100, 100])     # Definindo os valores máx e min a serem plotados
plt.ylabel('Ângulo Máximo/Mínimo (graus)')     # Definindo a label do eixo y
plt.xlabel('Tempo (s)')     # Definindo a label do eixo x
plt.title('Chumbo')     # Definindo o título
plt.show()     # Faz o gráfico aparecer
