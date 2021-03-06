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
- A bolinha só perde energia em seu moviento segundo o atrito com o ar;
- A corda que sustenta a bolinha é ideal: sem massa e incapaz de se deformar;
"""

# IMPORTANDO AS BIBLIOTECAS NECESSÁRIAS:

from Parametros import *

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace

'''
Iteração 3

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

def aluminio(v,t):
    dydt = v[1]
    dzdt = ((mAluminio*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mAluminio*l)
    return [dydt, dzdt]

def ferro(v,t):
    dydt = v[1]
    dzdt = ((mFerro*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mFerro*l)
    return [dydt, dzdt]

def prata(v,t):
    dydt = v[1]
    dzdt = ((mPrata*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mPrata*l)
    return [dydt, dzdt]

def ouro(v,t):
    dydt = v[1]
    dzdt = ((mOuro*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mOuro*l)
    return [dydt, dzdt]

def platina(v,t):
    dydt = v[1]
    dzdt = ((mPlatina*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mPlatina*l)
    return [dydt, dzdt]

lista_materiais = [chumbo, aluminio, ferro, prata, ouro, platina]


    # DEFININDO OS PARÂMETROS A SEREM UTILIZADOS NO CÁLCULO:

Tinicial = 0    # Tempo inicial
Tfinal = 50000    # Tempo final
Nmed = (Tfinal*10)+1  # Número de medições no intervalo de tempo

TPM = Tfinal/Nmed     # Tempo por medição (s)

T = linspace(Tinicial, Tfinal, Nmed)  # criando a lista de tempo e o número de medições nesse intervalo de tempo

    # CRIANDO A LITSA DE ÂNGULOS PARA O GRÁFICO (EIXO X):

Agrafico = []
for i in range(19):
    a = -90 + i*5
    Agrafico.append(a)


    # CALCULANDO OS VALORES DO TEMPO DE ESTABILIZAÇÃO DO PÊNDULO (EIXO Y):

Vchumbo = []
Valuminio = []
Vferro = []
Vprata = []
Vouro = []
Vplatina = []
for f in lista_materiais:

    print('')

    if f == chumbo:
        print('MÓDULO "CHUMBO"')

    elif f == aluminio:
        print('MÓDULO "ALUMÍNIO"')

    elif f == ferro:
        print('MÓDULO "FERRO"')

    elif f == prata:
        print('MÓDULO "PRATA"')

    elif f == ouro:
        print('MÓDULO "OURO"')

    elif f == platina:
        print('MÓDULO "PLATINA"')

    else:
        print('MÓDULO INEXISTENTE')

    for i in range(19):

        print(int((1/19*(i+1)) * 100), '% concluído')
        print('')

        y0 = (math.pi/2) + (i*((math.pi/180)*5))
        z0 = 0
        V0 = [y0, z0]

        if f == platina:
            T = linspace(Tinicial, 65000, 650001)

        else:
            pass

        Z = odeint(f, V0, T)

        for e in Z:
            e[0] = pi_rad(e[0])
            e[0] = e[0] - 180

        Tstop = []

        for x in range(1, len(Z)-1):

            if Z[x][0] <= 2:
                if Z[x][0] > Z[x+1][0]:
                    if Z[x][0] > Z[x-1][0]:
                        Tstop.append(x*TPM)

            else:
                pass


        if f == chumbo:
            Vchumbo.append(Tstop[0])

        elif f == aluminio:
            Valuminio.append(Tstop[0])

        elif f == ferro:
            Vferro.append(Tstop[0])

        elif f == prata:
            Vprata.append(Tstop[0])

        elif f == ouro:
            Vouro.append(Tstop[0])

        elif f == platina:
            Vplatina.append(Tstop[0])

        else:
            pass


#======================================================================================================================#

# PLOTANDO OS DADOS:

plt.plot(Agrafico, Valuminio)   # Definindo quais variaveis serão plotados
plt.plot(Agrafico, Vchumbo)
plt.plot(Agrafico, Vferro)
plt.plot(Agrafico, Vprata)
plt.plot(Agrafico, Vouro)
plt.plot(Agrafico, Vplatina)
plt.axis([-90, 0, 0, max(Vplatina)+500])     # Definindo os valores máx e min a serem plotados
plt.ylabel('Tempo(s)')     # Definindo a label do eixo y
plt.xlabel('Ângulo (graus)')     # Definindo a label do eixo x
plt.title('Tempo X Ângulo')     # Definindo o título
plt.show()     # Faz o gráfico aparecer