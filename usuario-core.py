class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.account_balance = 0

    def make_deposit(self, cuenta):	
        self.account_balance += cuenta
        return self.account_balance

    def make_withdrawal (self, cuenta):
        self.account_balance -= cuenta
        return self.account_balance

    def display_user_balance (self) : 
        return f"Usuario: {self.nombre}, Saldo:  {self.account_balance}"
    #def transfer_money (self, other_user, monto):

    def transfer_money (self, receptor, monto):
        if self.account_balance>= monto:
            self.account_balance -= monto
            receptor.account_balance += monto
        else: print("Saldo insuficiente para realizar la transferencia")
        return self

usuario1 = Usuario("Yamy", "yamy@gmail.com")
usuario2 = Usuario("Yo", "micuenta@gmail.com")
usuario3 = Usuario("Tu", "otracuenta@gmail.com")

usuario1.make_deposit(1000)
usuario1.make_deposit(50)
usuario1.make_deposit(2896)
print(usuario1.display_user_balance())

usuario2.make_deposit(8000)
usuario2.make_deposit(50)
usuario2.make_withdrawal(1600)
usuario2.make_withdrawal(50)
print(usuario2.display_user_balance())

usuario3.make_deposit(3000)
usuario3.make_withdrawal(289)
usuario3.make_withdrawal(50)
usuario3.make_withdrawal(45)
print(usuario3.display_user_balance())

#BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera 
# dinero al tercer usuario y luego imprima los saldos de ambos usuarios
