class CuentaBancaria:
    todas_las_cuentas = []
    def __init__(self, numero_cuenta, tasa_interes, balance):
        self.numero_cuenta = numero_cuenta
        self.tasa_interes = tasa_interes
        self.balance = balance          
        CuentaBancaria.todas_las_cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance < amount:
            print("Fondos insuficientes: cobrando una tarifa de $5")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f"Balance $ {self.balance}")
        return self
        
    def generar_interes(self):
        if self.balance > 0:
            self.newbalance = self.balance * self.tasa_interes
            self.balance = float(self.balance + self.newbalance)        
        return self
    
    def imprimir_todas_las_cuentas(cls):
        for cuenta in cls.todas_las_cuentas:
            print("Balance", cuenta.balance)
            return cls


class Usuario:
    def __init__(self, name, email,numero_cuenta):
        self.name = name
        self.email = email
        self.mis_cuentas = []
        self.cuenta = CuentaBancaria(numero_cuenta,tasa_interes=0.02,balance=0)
        self.mis_cuentas.append(self.cuenta)

    def hacer_deposito(self,amount):
        self.cuenta.deposito(amount)
        return self
    
    def hacer_retiro(self,amount):
        self.cuenta.retiro(amount)
        return self
    
    def mostrar_balance_usuario(self):
        self.cuenta.mostrar_info_cuenta()
        return self

    def abrir_nueva_cuenta(self, numero_cuenta):
        nueva_cuenta = CuentaBancaria(numero_cuenta, tasa_interes=0.02, balance=0)
        self.mis_cuentas.append(nueva_cuenta)
        return self
    
    def hacer_deposito_en_cuenta(self, numero_cuenta, monto):
        for self.cuenta in self.mis_cuentas:            
            if self.cuenta.numero_cuenta == numero_cuenta:                
                self.cuenta.deposito(monto)
        return self
    
    def mostrar_info_cuentas_usuario(self):
        for cuenta in self.mis_cuentas:
            print(f" La cuenta #{cuenta.numero_cuenta} del cliente {self.name} tiene un balance de $ {cuenta.balance}")
        return self

usuario1 = Usuario("Kate","katef@royal.uk", 111)
usuario2 = Usuario("Carlos","carlos@theking.uk", 222)

usuario1.hacer_deposito(1000).hacer_deposito(1000).hacer_deposito(2225).mostrar_balance_usuario()
usuario2.hacer_deposito(5000).hacer_deposito(4500).hacer_retiro(1350).mostrar_balance_usuario()

usuario2.abrir_nueva_cuenta(333).hacer_deposito_en_cuenta(333,6000).mostrar_info_cuentas_usuario()

# kate = CuentaBancaria(0.01,0)
# carlos = CuentaBancaria (0.01,0)

# kate.deposito(1000).deposito(1000).deposito(2225).generar_interes().mostrar_info_cuenta()
# carlos.deposito(5000).deposito(4500).retiro(250).retiro(100).retiro(1000).retiro(125).generar_interes().mostrar_info_cuenta()

# CuentaBancaria.imprimir_todas_las_cuentas(kate)
# CuentaBancaria.imprimir_todas_las_cuentas(carlos)