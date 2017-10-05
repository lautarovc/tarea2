'''
Universidad Simon Bolivar
Laboratorio de Ingenieria de Software
Pruebas de Tarea 2

Autores:
   - Yarima Luciani 13-10770
   - Lautaro Villalon 12-10427
'''

import unittest

from tarea2 import *

class Test(unittest.TestCase):

    # Duracion de servicio de 00:15:00
    
    def testBordeInferior(self):
        tarifa = Tarifa(10,15)
        desde = datetime(2017,10,1,2,0,0)
        hasta = datetime(2017,10,1,2,15,0)
        
    # Duracion de servicio 7 dias exactos
    
    def testBordeSuperior(self):
        tarifa = Tarifa(10,15)
        desde = datetime(2017,10,1,0,0,0)
        hasta = datetime(2017,10,8,0,0,0)
        
    # Duracion de servicio de 00:14:59
    
    def testFueraDominioMinimo(self):
        tarifa = Tarifa(10,15)
        desde = datetime(2017,10,1,2,0,0)
        hasta = datetime(2017,10,1,2,14,59)
        
    # Duracion de servicio de 7 dias y 00:00:01
    
    def testFueraDominioMaximo(self):
        tarifa = Tarifa(10,15)
        desde = datetime(2017,10,1,0,0,0)
        hasta = datetime(2017,10,8,0,0,1)

    # Duracion de servicio 7 dias con tarifa 0
    
    def testEsquinaInfDer(self):
        tarifa = Tarifa(0,0)
        desde = datetime(2017,10,1,0,0,0)
        hasta = datetime(2017,10,8,0,0,0)
        
    # Duracion de servicio 15 min con tarifa 0    
    
    def testEsquinaInfIzq(self):
        tarifa = Tarifa(0,0)
        desde = datetime(2017,10,1,0,0,0)
        hasta = datetime(2017,10,1,0,15,0) 

    # Servicio de Sabado a Martes (Usando ambas tarifas)
    
    def testMalicia1(self):
        tarifa = Tarifa(10,15)
        desde = datetime(2017,10,7,14,0,0)
        hasta = datetime(2017,10,10,10,0,0)
        
    # Servicio Invertido
    
    def testMalicia2(self):
        tarifa = Tarifa(10,15)
        desde = datetime(2017,10,5,14,0,0)
        hasta = datetime(2017,10,1,0,0,0)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()