class Billetes():
    def __init__(self):
        self.denominacion = None
        self.moneda = None
        self.representacion = None
    
class billete100(Billetes):
    def __init__(self):
        self.Valores()

    def Valores(self):
        self.denominacion = 100
        self.moneda = "pesos"
        self.representacion = "$100"

class billete200(Billetes):
    def __init__(self):
        self.Valores()

    def Valores(self):
        self.denominacion = 200
        self.moneda = "pesos"
        self.representacion = "$200"

class billete500(Billetes):
    def __init__(self):
        self.Valores()

    def Valores(self):
        self.denominacion = 500
        self.moneda = "pesos"
        self.representacion = "$500"

class billete1000(Billetes):
    def __init__(self):
        self.Valores()

    def Valores(self):
        self.denominacion = 1000
        self.moneda = "pesos"
        self.representacion = "$1000"