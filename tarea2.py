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

class Tarifa:
    def __init__(self, diaS, diaF):
        try:
            assert((diaS >= 0) and (diaF >= 0))
            
        except:
            print("La tarifa debe ser en numeros positivos.")
            sys.exit()
            
        self.diaSemana = diaS
        self.diaFin = diaF
        
   
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

def diasDeFin(tiempoDeServicio):
    delta = tiempoDeServicio[1] - tiempoDeServicio[0]
    
    dias = []
 
    for x in range(1, delta.days):
        dias.append(tiempoDeServicio[0] + timedelta(x))
     
    suma = 0
    
    for dia in dias:
        if (dia.weekday() >= 5):
            suma += 1
        
        
    return suma
  

def calcularPrecio(tarifa, tiempoDeServicio):
    
    delta = tiempoDeServicio[1] - tiempoDeServicio[0]
    
    # Comprobamos que el tiempo de servicio sea mayor a 15 minutos.
    try:
        assert(delta.days != 0 or (delta.seconds/60) >= 15)
        
    except:
        print("La duracion del servicio debe ser mayor o igual a 15 minutos.")
        sys.exit()
        
    # Comprobamos que el tiempo de servicio sea maximo 7 dias.
    
    try:
        assert(delta.days <= 7 or (delta.days != 7 or delta.seconds == 0))
    
    except:
        print("La duracion del servicio debe ser maximo de 7 dias.")
        sys.exit()        
    
    
    # Analizamos y calculamos el primer dia.
    
    temp = tiempoDeServicio[0] + timedelta(days=1)
    
    primerDia = datetime(temp.year, temp.month, temp.day) - tiempoDeServicio[0]
    
    if (tiempoDeServicio[0].weekday() < 5):
        precioDia0 = math.ceil(primerDia.seconds/3600.0)*tarifa.diaSemana
    
    else:
        precioDia0 = math.ceil(primerDia.seconds/3600.0)*tarifa.diaFin
        
     
    # Analizamos y calculamos el ultimo dia.
    
    ultimoDia = tiempoDeServicio[1] - datetime(tiempoDeServicio[1].year, tiempoDeServicio[1].month, tiempoDeServicio[1].day)
    
    if (tiempoDeServicio[1].weekday() < 5):
        precioDiaF = math.ceil(ultimoDia.seconds/3600.0)*tarifa.diaSemana
        
    else:
        precioDiaF = math.ceil(ultimoDia.seconds/3600.0)*tarifa.diaFin
        
        
    # Analizamos y calculamos todos los dias intermedios.
    
    diasIntermedios = diasDeSemana(tiempoDeServicio)
    
    diasFines = diasDeFin(tiempoDeServicio)
    
    precioIntermedios = (diasIntermedios*24*tarifa.diaSemana) + (diasFines*24*tarifa.diaFin)
    
    
    # Calculamos el precio total
    
    precioTotal = precioDia0 + precioIntermedios + precioDiaF
    
    return precioTotal
        
tarifa = Tarifa(10, 15)

desde = datetime(2017,10,8,23,59,2)
hasta = datetime(2017,10,9,9,1,2)

tiempos = [desde, hasta]
    
print(calcularPrecio(tarifa, tiempos))
