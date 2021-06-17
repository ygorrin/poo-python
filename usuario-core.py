#make_withdrawal (self, amount) : haz que este método disminuya el saldo del usuario en la cantidad especificada
#display_user_balance (self) : haz que este método imprima el nombre del usuario y el saldo de la cuenta en el terminal
#p.ej. "Usuario: Guido van Rossum, Saldo: $ 150
#BONIFICACIÓN: transfer_money (self, other_user, amount) : haz que este método disminuya el saldo del usuario en la cantidad y agrega esa cantidad al saldo de otro other_user
# Crea un archivo con la clase Usuario, incluidos los métodos __init__ y make_deposit
# Agrega un método make_withdrawal a la clase Usuario
# Agrega un método display_user_balance a la clase Usuario
# Crea 3 instancias de la clase de usuario
# Haz que el primer usuario haga 3 depósitos y 1 retiro y luego muestre su saldo
# Haz que el segundo usuario haga 2 depósitos y 2 retiros y luego muestre su saldo
# Haz que el tercer usuario haga 1 depósitos y 3 retiros y luego muestre su saldo
# BONIFICACIÓN: Agrega un método transfer_money; haga que el primer usuario transfiera dinero al tercer usuario y luego imprima los saldos de ambos usuarios

class Usuario:# aqui está lo que tenemos hasta ahora
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.account_balance = 0
    # agrega el método deposit
    def make_deposit(self, cuenta):	# toma un argumento que es el monto del depósito
        self.account_balance += cuenta	# la cuenta del usuario específico aumenta por la cantidad del valor recibido
        return self.account_balance
    def make_withdrawal (self, cuenta): #haz que este método disminuya el saldo del usuario en la cantidad
        self.account_balance -= cuenta
        return self.account_balance
    def display_user_balance (self) : 
        return f"Usuario: {self.nombre}, Saldo:  {self.account_balance}"
    #def transfer_money (self, other_user, monto):

    def transfer_money (self, emisor, receptor, monto):
        self.emisor.Usuario() = emisor
        self.receptor.Usuario() = receptor
        self.monto = monto
        self.emisor.Usuario().make_withdrawal(monto)
        self.receptor.Usuario().make_deposit(monto)
        return f"El ususario {self.emisor.Usuario().nombre} transfirió {self.monto}  saldo {emisor.display_user_balance()} n/al usuario {self.receptor.Usuario().nombre} n/"


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

transfer_money(usuario1.nombre, usuario2.nombre, 300 )
