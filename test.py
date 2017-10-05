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
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()