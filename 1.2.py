#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 12:39:04 2020

@author: sebas
"""

import numpy as np

r = [-2,3,5]

def g(s1,s2):
    return r[s1]+r[s2]

p = [[0.5,1/3,1/6],
     [0,3/4,1/4],
     [0,0,1]
     ]

# p2 = np.dot(p,p)

# Analíticamente
E1a = 0
for i in range(3):
    for j in range(3):
        E1a += g(i,j)*p[0][i]*p[i][j]
        
print(E1a)


#Simulación
vals=[]
def dosPasos():
    s1 = np.random.choice(3, 1, False, p[0])
    s2 = np.random.choice(3, 1, False, p[s1[0]])
    return g(s1[0],s2[0])

epocas = 10
for _ in range(epocas):
    for i in range(10000):
        vals.append(dosPasos())
    E1s = sum(vals)/len(vals)
    print(E1s)