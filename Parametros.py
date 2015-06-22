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

l = 0.1 + R #(m)

Vesf = 4/3 * math.pi * R**3 #(m3)

mAluminio = dAluminio * Vesf    # Massa da bolinha
mChumbo = dChumbo * Vesf    # Massa da bolinha
mFerro = dFerro * Vesf    # Massa da bolinha
mOuro = dOuro * Vesf    # Massa da bolinha
mPlatina = dPlatina * Vesf    # Massa da bolinha
mPrata = dPrata * Vesf    # Massa da bolinha