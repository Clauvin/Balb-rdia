# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 12:48:47 2016

@author: Rafael França
"""

import CPUtimer

# Função a ser cronometrada:
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
    
# Instanciano a CPU timer  
timer = CPUtimer.CPUTimer()


# Função wrapper para fazer instrumentação automatica
def w_fib():
    return fib(10)
    

# Medindo código curto/rapido executando diversas vezes de forma automatica
print("")
print("Medindo codigo rápido repetido diversas vezes:")
timer.auto_loop( w_fib , 100000)

# Imprimindo resultados de diversas formas
print("Tempo Total: " + str( timer.get_time() ) +" s")
print("Tempo Medio: " + str( timer.get_time("average","micro") ) +" \u00B5s")
print("Ultima Chamada: " + str( timer.get_time("last","micro") ) +" \u00B5s")
print("Estampa 1 do total: " + str( timer.get_stamp("total","si") ) ) 
print("Estampa 2 do total: " + str( timer.get_stamp("total","clock") ) )

# TODO: Implementar exemplo usando o functools.partial(foo, A, B)