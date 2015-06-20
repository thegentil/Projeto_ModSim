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

from Parâmetros import *

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace 

'''
Iteração 2

Considerações Especificas:
 
- O pêndulo é constituido por apenas uma bolinha.
- Consideramos diferentes materiais para as bolinha (O que altera, portanto, a densidade e 
  massa de cada uma das bolinhas)

'''

# DEFININDO OS PARÂMETROS A SEREM UTILIZADOS NO CÁLCULO:

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]

Tinicial = 0    # Tempo inicial
Tfinal = 50000    # Tempo final
Nmed = (Tfinal*10)+1  # Número de medições no intervalo de tempo

TPM = Tfinal/Nmed     # Tempo por medição (s)

T = linspace(Tinicial, Tfinal, Nmed)  # criando a lista de tempo e o número de medições nesse intervalo de tempo

#======================================================================================================================#

# DEFININDO AS FUNÇÕES PARA CADA MATERIAL:

    # ALUMÍNIO:

def aluminio(v,t):
    dydt = v[1]
    dzdt = ((mAluminio*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mAluminio*l)
    return [dydt, dzdt]

    # CHUMBO:

def chumbo(v,t):
    dydt = v[1]
    dzdt = ((mChumbo*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mChumbo*l)
    return [dydt, dzdt]

    # FERRO:

def ferro(v,t):
    dydt = v[1]
    dzdt = ((mFerro*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mFerro*l)
    return [dydt, dzdt]

    # OURO:

def ouro(v,t):
    dydt = v[1]
    dzdt = ((mOuro*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mOuro*l)
    return [dydt, dzdt]

    # PLATINA:

def platina(v,t):
    dydt = v[1]
    dzdt = ((mPlatina*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mPlatina*l)
    return [dydt, dzdt]

    # PRATA:

def prata(v,t):
    dydt = v[1]
    dzdt = ((mPrata*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mPrata*l)
    return [dydt, dzdt]

#======================================================================================================================#

# FAZENDO OS CÁLCULOS E PLOTANDO OS DADOS:

lista_funcoes = [aluminio, chumbo, ferro, ouro, platina, prata] # definindo uma lista com o nome das funções

for f in lista_funcoes:     # fazendo um for loop para criar fazer os cálculos e plotar os dados obtidos

    Z = odeint(f, V0, T)

    for e in Z:
        e[0] = pi_rad(e[0])
        e[0] = e[0] - 180

    plt.plot(T, Z[:, 0])     # Definindo quais variaveis serão plotados
    plt.axis([0, max(T), -100, 100])     # Definindo os valores máx e min a serem plotados
    plt.ylabel('Ângulo (graus)')     # Definindo a label do eixo y
    plt.xlabel('Tempo (s)')     # Definindo a label do eixo x
    plt.title(str(f).upper())     # Definindo o título
    plt.show()     # Faz o gráfico aparecer


