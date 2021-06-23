
# nombre en singular y la primera letra en mayuscula



class Usuario:
    def __init__(self, nombre, apellido, email):  # constructor
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.balance_cuenta = 0
        self.rol = "NORMAL"
        self.registrarLog("objeto creado")

    def getBalance(self):
        self.registrarLog("el usuario solicito un balance.")
        return f"{self.nombre} {self.apellido} - SALDO: $ {self.balance_cuenta}"

    def hacer_deposito(self, monto):
        self.balance_cuenta += monto
        self.registrarLog(f"el usuario acaba de registrar {monto} a {self.nombre} quedando : {self.getBalance()}")
        return self


    def hacer_giro(self, monto):
        if self.balance_cuenta < monto:
            print(f"NO TIENE SALDO SUFIENTE- SALDO: {self.balance_cuenta} falta: { monto - self.balance_cuenta } ")
            return self
        self.balance_cuenta -= monto
        self.registrarLog(f"el usuario acaba de registrar {monto} a {self.nombre} quedando : {self.getBalance()}")
        return self
    
    def registrarLog(self, mensaje):
        f = open("log_de_depositos.txt","a",encoding="utf8")
        f.write(mensaje + "\n")
        f.close()
        return self

    def transferencia(self, usuario_destino, monto):
        if self.balance_cuenta < monto:
            print(f"NO TIENE SALDO SUFIENTE {self.nombre}- SALDO: {self.balance_cuenta} falta: { monto - self.balance_cuenta } ")
            return self

        self.hacer_giro(monto)
        usuario_destino.hacer_deposito(monto)

        return self


    def calcularSaldo(self, monto):
        pass

    def __str__(self): 
        self.registrarLog("El usuario imprimio el objeto usuario")
        return "Objeto Usuario:\t" + self.nombre + " " + self.apellido

usuario1 = Usuario("FRANCISCO","BOISIER", "jajq@jaja.com")

print(usuario1)
usuario1.hacer_deposito(1000).hacer_deposito(500).hacer_giro(5000)
print(usuario1.getBalance())

usuario2 = Usuario("JAVIER", "Sandoval", "jeje@jeje.com")
print(usuario2)
usuario2.hacer_deposito(200)
print(usuario2.getBalance())

usuario3 = Usuario("FRANCISCO", "LOL", "jojojo@jojo.com")
print(usuario3)

pancho = Usuario("Pancho","Boisier","jajqa@gmail.com")
pancho.hacer_deposito(1000)
print(pancho.getBalance())

javier = Usuario("Javier", "Sandoval", "jeje@jaja.com")
javier.hacer_deposito(1000)
print(javier.getBalance())

pancho.transferencia(javier, 500)

print(pancho.getBalance())
print(javier.getBalance())


class Gato:
    def __init__(self, nombre_gato="", raza="Kiltro", patas=4):
        self.nombre = nombre_gato
        self.raza = raza
        self.patas = patas
    
    def __str__(self):
        return f"El nombre del GATO es {self.nombre}, y es de raza {self.raza} y tiene {self.patas} patas"

minino = Gato("Minino", "Guerrero")
print(minino)

zora = Gato("Zora", "Pirata")
print(zora)

cualquiera = Gato("Don Gato",patas=3)
print(cualquiera)