'''
Universidad Simon Bolivar
Laboratorio de Ingenieria de Software
Tarea 2

Autores:
   - Yarima Luciani 13-10770
   - Lautaro Villalon 12-10427
'''

import sys, math
from datetime import datetime, timedelta
   
def diasDeSemana(tiempoDeServicio):
    delta = tiempoDeServicio[1] - tiempoDeServicio[0]
    
    dias = []
 
    for x in range(1, delta.days):
        dias.append(tiempoDeServicio[0] + timedelta(x))
     
    suma = 0
    
    for dia in dias:
        if (dia.weekday() < 5):
            suma += 1
        
        
    return suma
