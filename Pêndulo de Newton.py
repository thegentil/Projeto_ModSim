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
- Temperatura do ar em 25˚C

"""
# Importando as bibliotecas necessárias:

import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace 
import math

# Convertendo de Radianos para Graus

def pi_rad(rad):
    x = (180 * rad)/math.pi
    return x

# Parâmetros iniciais:

R = 0.01 #(m)

dAluminio = 2697 #(kg/m3)

dChumbo = 11340 #(kg/m3)

dFerro = 7870 #(kg/m3)

dOuro = 19280 #(kg/m3)

dPlatina = 21450 #(kg/m3)

dPrata = 10500 #(kg/m3)

g = 10 #(m/s2)

dAr = 1.184 #(kg/m3)

A = math.pi * (R**2) #(m2)

k = 0.47 * 0.5 * A * dAr

l = 0.1 + R

Vesf = 4/3 * math.pi * R**3 #(m3)

mAluminio = dAluminio * Vesf    # Massa da bolinha   
mChumbo = dChumbo * Vesf    # Massa da bolinha
mFerro = dFerro * Vesf    # Massa da bolinha
mOuro = dOuro * Vesf    # Massa da bolinha
mPlatina = dPlatina * Vesf    # Massa da bolinha
mPrata = dPrata * Vesf    # Massa da bolinha

'''
Iteração 1

Considerações Especificas:
 
- O pêndulo é constituido por apenas uma bolinha.
- Consideramos que a bolinha é de Chumbo

'''

# Função da derivada

def chumbo(v,t):
    dydt = v[1]
    dzdt = ((mChumbo*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mChumbo*l)
    return [dydt, dzdt]

# Parâmetros iniciais, linspace(gerar lista de tempo), odeint(calcula a derivada)

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(chumbo,V0,T)

# Tranformando de radiano para graus e ajustando para que plote os valores certos

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'g')     # Definindo quais variaveis serão plotados
plt.axis([0, max(T), -90, 90])     # Definindo os valores máx e min a serem plotados
plt.ylabel('Ângulo (Em graus)')     # Definindo a label do eixo y
plt.xlabel('t')     # Definindo a label do eixo x
plt.title('Chumbo')     # Definindo o título
plt.show()     # Faz o gráfico

'''
Iteração 2

Considerações Especificas:
 
- O pêndulo é constituido por apenas uma bolinha.
- Consideramos diferentes materiais para as bolinha (O que altera, portanto, a densidade e 
  massa de cada uma das bolinhas)

'''

# Aluminio

def aluminio(v,t):
    dydt = v[1]
    dzdt = ((mAluminio*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mAluminio*l)
    return [dydt, dzdt]

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(aluminio,V0,T)

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'r')
plt.axis([0, max(T), -90, 90])
plt.ylabel('Ângulo (Em graus)')
plt.xlabel('t')
plt.title('Aluminio')
plt.show()

# Chumbo

def chumbo(v,t):
    dydt = v[1]
    dzdt = ((mChumbo*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mChumbo*l)
    return [dydt, dzdt]

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(chumbo,V0,T)

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'g')
plt.axis([0, max(T), -90, 90])
plt.ylabel('Ângulo (Em graus)')
plt.xlabel('t')
plt.title('Chumbo')
plt.show()

# Ferro

def ferro(v,t):
    dydt = v[1]
    dzdt = ((mFerro*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mFerro*l)
    return [dydt, dzdt]

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(ferro,V0,T)

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'b')
plt.axis([0, max(T), -90, 90])
plt.ylabel('Ângulo (Em graus)')
plt.xlabel('t')
plt.title('Ferro')
plt.show()

# Ouro

def ouro(v,t):
    dydt = v[1]
    dzdt = ((mOuro*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mOuro*l)
    return [dydt, dzdt]

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(ouro,V0,T)

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'r')
plt.axis([0, max(T), -90, 90])
plt.ylabel('Ângulo (Em graus)')
plt.xlabel('t')
plt.title('Ouro')
plt.show()

# Platina

def platina(v,t):
    dydt = v[1]
    dzdt = ((mPlatina*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mPlatina*l)
    return [dydt, dzdt]

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(platina,V0,T)

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'g')
plt.axis([0, max(T), -90, 90])
plt.ylabel('Ângulo (Em graus)')
plt.xlabel('t')
plt.title('Platina')
plt.show()

# Prata

def prata(v,t):
    dydt = v[1]
    dzdt = ((mPrata*g*math.sin(v[0])) - (k*(l**2)*(v[1]*((v[1]**2)**0.5))))/(mPrata*l)
    return [dydt, dzdt]

y0 = math.pi/2
z0 = 0
V0 = [y0, z0]
T = linspace(0,50000,500001)
Z = odeint(prata,V0,T)

for e in Z:
    e[0] = pi_rad(e[0])
    e[0] = e[0] - 180

print(Z)

plt.plot(T, Z[:,0],'')
plt.axis([0, max(T), -90, 90])
plt.ylabel('Ângulo (Em graus)')
plt.xlabel('t')
plt.title('Prata')
plt.show()






