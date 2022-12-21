class Usuario:
    def __init__(self, name, email, balance_cuenta):
        self.name = name
        self.email = email
        self.balance_cuenta = balance_cuenta
    
    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self
    
    def hacer_retiro(self,amount):
        self.balance_cuenta -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"El usuario {self.name} tiene $ {self.balance_cuenta} pesos en su cuenta")
        return self

    def transferir_dinero(self, recibe, amount):
        self.hacer_retiro(amount)
        recibe.hacer_deposito(amount)
        return self


kate = Usuario("Kate Fidd", "k.fidd@royalemail.uk",0)
meghan = Usuario("Meghan Narle", "meghan_narle@gmail.com",0)
carlos = Usuario("Carlos King", "the.king@king.uk",0)

#1
kate.hacer_deposito(1000).hacer_deposito(2000).hacer_deposito(3000).hacer_retiro(500).mostrar_balance_usuario()

#2
meghan.hacer_deposito(3000).hacer_deposito(1500).hacer_retiro(1000).hacer_retiro(700).mostrar_balance_usuario()

#3
carlos.hacer_deposito(5000).hacer_retiro(300).hacer_retiro(600).hacer_retiro(1200).mostrar_balance_usuario()

#4
kate.transferir_dinero(carlos,500).mostrar_balance_usuario()
carlos.mostrar_balance_usuario()