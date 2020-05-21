from Billetes import *

class Cajero():
    def __init__(self):
        self.verificacion = 0
        self.a = True
        self.fondos = 0
        self.monto = 0
        self.exctraccion = []
        self.cantBilletes = {
            #[cantBill, valorTotal]
            "$100": [0, 0],
            "$200": [0, 0],
            "$500": [0, 0],
            "$1000": [0, 0]
        }

    def agregarDinero(self, cantDinero):
        for bill in cantDinero:
            if bill.representacion == "$100":
                self.cantBilletes["$100"][0] += 1
                self.cantBilletes["$100"][1] += bill.denominacion
                self.fondos += bill.denominacion

            elif bill.representacion == "$200":
                self.cantBilletes["$200"][0] += 1
                self.cantBilletes["$200"][1] += bill.denominacion
                self.fondos += bill.denominacion
            
            elif bill.representacion == "$500":
                self.cantBilletes["$500"][0] += 1
                self.cantBilletes["$500"][1] += bill.denominacion
                self.fondos += bill.denominacion

            elif bill.representacion == "$1000":
                self.cantBilletes["$1000"][0] += 1
                self.cantBilletes["$1000"][1] += bill.denominacion
                self.fondos += bill.denominacion

    def contarDinero(self):
        #100 200 500 1000
        cont = [[0, 0], [0, 0], [0, 0], [0, 0]]
        if self.cantBilletes["$100"][0] != 0:
            cont[0][0] = self.cantBilletes["$100"][0]
            cont[0][1] = self.cantBilletes["$100"][1]
        if self.cantBilletes["$200"][0] != 0:
            cont[1][0] = self.cantBilletes["$200"][0]
            cont[1][1] = self.cantBilletes["$200"][1]
        if self.cantBilletes["$500"][0] != 0:
            cont[2][0] = self.cantBilletes["$500"][0]
            cont[2][1] = self.cantBilletes["$500"][1]
        if self.cantBilletes["$1000"][0] != 0:
            cont[3][0] = self.cantBilletes["$1000"][0]
            cont[3][1] = self.cantBilletes["$1000"][1]

        a = "Hay " + str(cont[0][0]) + " billetes de 100, total: " + str(cont[0][1]) + "\n" + "Hay " + str(cont[1][0]) + " billetes de 200, total: " + str(cont[1][1]) + "\n" + "Hay " + str(cont[2][0]) + " billetes de 500, total: " + str(cont[2][1]) + "\n" + "Hay " + str(cont[3][0]) + " billetes de 1000, total: " + str(cont[3][1]) + "\n" + "Total: "+ str(self.fondos)

        return str(a)
    
    def cambio(self, cambio):
        if cambio >= 100 and self.cantBilletes["$100"][0] != 0:
            while self.cantBilletes["$100"][0] != 0 and cambio >= 100:
                self.cantBilletes["$100"][0] -= 1
                self.cantBilletes["$100"][1] -= 100
                self.fondos -= 100
                cambio -= 100
                self.monto -= 100
                self.exctraccion.append("$100")

        if cambio >= 200 and self.cantBilletes["$200"][0] != 0:
            while self.cantBilletes["$200"][0] != 0 and cambio >= 200:
                self.cantBilletes["$200"][0] -= 1
                self.cantBilletes["$200"][1] -= 200
                self.fondos -= 200
                cambio -= 200
                self.monto -= 200
                self.exctraccion.append("$200")

        if cambio >= 500 and self.cantBilletes["$500"][0] != 0:
            while self.cantBilletes["$500"][0] != 0 and cambio >= 500:
                self.cantBilletes["$500"][0] -= 1
                self.cantBilletes["$500"][1] -= 500
                self.fondos -= 500
                cambio -= 500
                self.monto -= 500
                self.exctraccion.append("$500")

        if cambio >= 1000 and self.cantBilletes["$1000"][0] != 0:
            while self.cantBilletes["$1000"][0] != 0 and cambio >= 1000:
                self.cantBilletes["$1000"][0] -= 1
                self.cantBilletes["$1000"][1] -= 100
                self.fondos -= 1000
                cambio -= 1000
                self.monto -= 1000
                self.exctraccion.append("$1000")

        if cambio != 0:
            cambio += 100
            self.cambio(cambio)
            return self.exctraccion

        self.extraerDinero(self.monto, False, 0)

    def calcularCambio(self, porcentaje):
        cambio = self.monto * (porcentaje / 100)
        if cambio < 100:
            cambio = 100
        else:
            cambio = int(100 * round(float(cambio)/100))
        self.cambio(cambio)
        return

    def extraerDinero(self, monto, cambio, porcentaje):
        self.monto = monto

        if monto < 0:
            raise Exception("El monto debe ser mayor a 0")
        if self.cantBilletes["$1000"][0] == 0 and self.cantBilletes["$500"][0] == 0 and self.cantBilletes["$200"][0] == 0 and self.cantBilletes["$100"][0] == 0:
            raise Exception("No hay billetes")
        if self.monto > self.fondos:
            raise Exception("No hay suficientes fondos")
        if self.monto%100 != 0:
            raise Exception("El monto no es multiplo de 100")
        if 0 > porcentaje or porcentaje > 100:
            raise Exception("El procentaje debe ir de 0 a 100")

        if self.a == True:
            self.verificacion = self.monto
            self.a = False
                
        if cambio == True and porcentaje < 100:
            self.calcularCambio(porcentaje)
            return self.exctraccion

        if self.monto >= 1000 and self.cantBilletes["$1000"][0] != 0:
            while self.cantBilletes["$1000"][0] != 0 and self.monto >= 1000:
                self.cantBilletes["$1000"][0] -= 1
                self.cantBilletes["$1000"][1] -= 100
                self.fondos -= 1000
                self.monto -= 1000
                self.exctraccion.append("$1000")

        if self.monto >= 500 and self.cantBilletes["$500"][0] != 0:
            while self.cantBilletes["$500"][0] != 0 and self.monto >= 500:
                self.cantBilletes["$500"][0] -= 1
                self.cantBilletes["$500"][1] -= 500
                self.fondos -= 500
                self.monto -= 500
                self.exctraccion.append("$500")

        if self.monto >= 200 and self.cantBilletes["$200"][0] != 0:
            while self.cantBilletes["$200"][0] != 0 and self.monto >= 200:
                self.cantBilletes["$200"][0] -= 1
                self.cantBilletes["$200"][1] -= 200
                self.fondos -= 200
                self.monto -= 200
                self.exctraccion.append("$200")

        if self.monto >= 100 and self.cantBilletes["$100"][0] != 0:
            while self.cantBilletes["$100"][0] != 0 and self.monto >= 100:
                self.cantBilletes["$100"][0] -= 1
                self.cantBilletes["$100"][1] -= 100
                self.fondos -= 100
                self.monto -= 100
                self.exctraccion.append("$100")

        if self.monto != 0:
            self.monto += 100
            self.extraerDinero(self.monto, False, 0)
        
        ver = ' '.join([str(elem) for elem in self.exctraccion])
        ver = ver.replace("$", "")
        ver = ver.split(" ")
        verif = 0
        for i in ver:
            verif += int(i)

        if verif == self.verificacion:
            return self.exctraccion
        else:
            raise Exception("No hay billetes para esa extraccion")