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


        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()