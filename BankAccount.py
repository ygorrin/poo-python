class CuentaBancaria:
    def __init__(self, numero, tasa = 0.1, saldo = 0):
        self.numero = numero
        self.tasa = tasa
        self.saldo = saldo

    def transferencia(self, recibe, monto):
        if self.saldo > monto:
            self.saldo -= monto
            recibe.saldo += monto
            print(f"""Transferencia realizado 
Cuenta Origen: {self.cuenta},
Monto: {self.monto}
Cuenta Destino: {self.recibe.numero}""")
        else: 
            print("Saldo insuficiente para hacer la transacción")
        return self

    def deposito(self, monto):
            self.saldo += monto
            print(f"Deposito realizado a la cuenta {self.numero} por un monto de: {monto}, Saldo: ${self.saldo}")
            return self

    def retiro(self, monto):
        if self.saldo > monto:
            self.saldo -= monto
            print(f"Retiro realizado a la cuenta {self.numero} por un monto de: {monto}, Saldo: ${self.saldo}")
        else: 
            print("Saldo insuficiente para hacer el retiro")
        return self

    def mostrarInformacionCuenta(self):
        print(f"Saldo: $ {self.saldo}")
        return self

    def sumaIntereses(self):
        self.saldo += self.saldo * self.tasa
        return self

    def __str__(self):
        return f"Tasa: {self.tasa}, Saldo: {self.saldo}" 

cuenta1 = CuentaBancaria(12345, 10, 15300)
cuenta2 = CuentaBancaria(54321, 5, 2300)

#En la primera cuenta, realice 3 depósitos y 1 retiro, luego calcule los intereses y muestre la 
# información de la cuenta en una sola línea de código (es decir, encadenamiento)
cuenta1.deposito(500).deposito(2000).deposito(300).retiro(25).mostrarInformacionCuenta()
#En la segunda cuenta, realice 2 depósitos y 4 retiros, luego calcule los intereses y muestre la 
# información de la cuenta en una sola línea de código (es decir, encadenamiento)
cuenta2.deposito(800).deposito(58).retiro(20).retiro(25).retiro(42).retiro(48).sumaIntereses().mostrarInformacionCuenta()


