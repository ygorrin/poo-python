class CuentaBancaria:
    def __init__(self, numero, tasa = 0.1, saldo = 0):
        self.numero = numero
        self.tasa = tasa
        self.saldo = saldo

    def mostrarInformacionCuenta(self):
        print(f"Saldo: $ {self.saldo}")
        return self

    def sumaIntereses(self):
        self.saldo += self.saldo * self.tasa
        return self

class Usuario:
    def __init__(self, nombre, cuenta):
        self.nombre = nombre
        self.cuenta = CuentaBancaria()

    def deposito(self, monto):
        self.saldo += monto
        print(f"Deposito realizado a la cuenta {self.cuenta.numero} por un monto de: {monto}, Saldo: ${self.cuenta.saldo}")
        return self

    def retiro(self, monto):
        if self.saldo > monto:
            self.saldo -= monto
            print(f"Retiro realizado a la cuenta {self.cuenta.numero} por un monto de: {monto}, Saldo: ${self.cuenta.saldo}")
        else: 
            print("Saldo insuficiente para hacer el retiro")
        return self

    def sumaIntereses(self):
        self.cuenta.saldo += self.cuenta.saldo * self.cuenta.tasa
        return self

    def mostrarInformacionCuenta(self):
        print(f"Saldo: $ {self.cuenta.saldo}")
        return self
    
    def transferencia(self, recibe, monto):
        if self.cuenta.saldo > monto:
            self.cuenta.saldo -= monto
            recibe.cuenta.saldo += monto
            print(f"""Transferencia realizado 
Cuenta Origen: {self.cuenta.numero},
Monto: {self.monto}
Cuenta Destino: {self.recibe.cuenta.numero}""")
        else: 
            print("Saldo insuficiente para hacer la transacción")
        return self

#SENSEI BONUS: Permite al usuario tener varias cuentas; 
# actualiza los metodos para que el usuario pueda especificar de 
# cual cuenta ellos quieren depositar o retirar


def registrarLog(self, mensaje):
        f = open("log_de_depositos.txt","a",encoding="utf8")
        f.write(mensaje + "\n")
        f.close()
        return self
