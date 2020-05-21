from Cajero import *
import unittest

class TestCargo1(unittest.TestCase):
    
    def setUp(self):
        self.cajero = Cajero()
        self.cajero.agregarDinero([
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000()
        ])

    def test_cargo1_a(self):
        self.assertEqual(self.cajero.contarDinero(), "Hay 0 billetes de 100, total: 0\nHay 0 billetes de 200, total: 0\nHay 0 billetes de 500, total: 0\nHay 10 billetes de 1000, total: 10000\nTotal: 10000")
    
    def test_cargo1_b(self):
        self.cajero.extraerDinero(5000, False, 0)
        self.assertEqual(self.cajero.exctraccion, ['$1000', '$1000', '$1000', '$1000','$1000'])
    
    def test_cargo1_c(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(12000, False, 0)
        self.assertEqual("No hay suficientes fondos", str(mens.exception))
    
    def test_cargo1_d(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(5520, False, 0)
        self.assertEqual(str(mens.exception), "El monto no es multiplo de 100")

class TestCargo2(unittest.TestCase):

    def setUp(self):
        self.cajero = Cajero()
        self.cajero.agregarDinero([
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000(),
        billete500(), billete500(), billete500(), billete500(), billete500(), 
        billete500(), billete500(), billete500(), billete500(), billete500(), 
        billete500(), billete500(), billete500(), billete500(), billete500(), 
        billete500(), billete500(), billete500(), billete500(), billete500()
        ])

    def test_cargo2_a(self):
        self.assertEqual(self.cajero.contarDinero(), "Hay 0 billetes de 100, total: 0\nHay 0 billetes de 200, total: 0\nHay 20 billetes de 500, total: 10000\nHay 10 billetes de 1000, total: 10000\nTotal: 20000")
        
    def test_cargo2_b(self):    
        self.cajero.extraerDinero(5000, False, 0)
        self.assertEqual(self.cajero.exctraccion, ['$1000', '$1000', '$1000', '$1000','$1000'])
        
    def test_cargo2_c(self):
        self.cajero.extraerDinero(12000, False, 0)
        self.assertEqual(self.cajero.exctraccion, ['$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$500', '$500', '$500', '$500'])

    def test_cargo2_d(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(12100, False, 0)
        self.assertEqual(str(mens.exception), "No hay billetes para esa extraccion")

    def test_cargo2_e(self):
        self.cajero.extraerDinero(7000, True, 10)
        self.assertEqual(self.cajero.exctraccion, ['$500', '$500', '$1000', '$1000','$1000', '$1000', '$1000','$1000'])

class TestCargo3(unittest.TestCase):

    def setUp(self):
        self.cajero = Cajero()
        self.cajero.agregarDinero([
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000(), billete1000(), billete1000(),
        billete1000(), billete1000(),
        billete500(), billete500(), billete500(), billete500(), billete500(), 
        billete500(), billete500(), billete500(), billete500(), billete500(), 
        billete500(), billete500(), billete500(), billete500(), billete500(), 
        billete500(), billete500(), billete500(), billete500(), billete500(),
        billete200(), billete200(), billete200(), billete200(), billete200(),
        billete200(), billete200(), billete200(), billete200(), billete200(),
        billete200(), billete200(), billete200(), billete200(), billete200()
        ])

    def test_no_porc(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(500, True, 101)
        self.assertEqual(str(mens.exception), "El procentaje debe ir de 0 a 100")

    def test_cargo3_a(self):
        self.assertEqual(self.cajero.contarDinero(), "Hay 0 billetes de 100, total: 0\nHay 15 billetes de 200, total: 3000\nHay 20 billetes de 500, total: 10000\nHay 10 billetes de 1000, total: 10000\nTotal: 23000")

    def test_cargo3_b(self):    
        self.cajero.extraerDinero(5000, False, 0)
        self.assertEqual(self.cajero.exctraccion, ['$1000', '$1000', '$1000', '$1000','$1000'])

    def test_cargo3_c(self):
        self.cajero.extraerDinero(12000, False, 0)
        self.assertEqual(self.cajero.exctraccion, ['$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$1000', '$500', '$500', '$500', '$500'])

    def test_cargo3_d(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(12100, False, 0)
        self.assertEqual(str(mens.exception), "No hay billetes para esa extraccion")

    def test_cargo3_e(self):
        self.cajero.extraerDinero(7000, True, 10)
        self.assertEqual(self.cajero.exctraccion, ['$200', '$200', '$200', '$200', '$1000', '$1000', '$1000', '$1000','$1000', '$1000', '$200'])

    

class TP3(unittest.TestCase):
    def setUp(self):
        self.cajero = Cajero()

    def test_dinero_negativo(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(-100, False, 0)
        self.assertEqual(str(mens.exception), "El monto debe ser mayor a 0")

    def test_no_billetes(self):
        with self.assertRaises(Exception) as mens:
            self.cajero.extraerDinero(100, False, 0)
        self.assertEqual(str(mens.exception), "No hay billetes")

if __name__ == "__main__":
    unittest.main()
