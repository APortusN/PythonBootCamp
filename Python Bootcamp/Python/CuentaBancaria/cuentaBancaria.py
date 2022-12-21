class CuentaBancaria:
    todas_las_cuentas = []
    def __init__(self, tasa_interes, balance):
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


kate = CuentaBancaria(0.01,0)
carlos = CuentaBancaria (0.01,0)

kate.deposito(1000).deposito(1000).deposito(2225).generar_interes().mostrar_info_cuenta()

carlos.deposito(5000).deposito(4500).retiro(250).retiro(100).retiro(1000).retiro(125).generar_interes().mostrar_info_cuenta()

CuentaBancaria.imprimir_todas_las_cuentas(kate)
CuentaBancaria.imprimir_todas_las_cuentas(carlos)