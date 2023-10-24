class Konto:
    def __init__(self):
        self.historia = []

    def przelew_wychodzacy(self,kwota):
        if self.saldo >= kwota and kwota > 0:
            self.saldo -= kwota
            self.historia.append(-kwota)
    def przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota
            self.historia.append(kwota)
    def przelew_express_wychodzacy(self,kwota):
        if kwota > 0 and kwota <self.saldo:
            self.saldo -= kwota
            self.saldo -= self.express_trasnfer_fee
            self.historia.append(-kwota)
            self.historia.append(-self.express_trasnfer_fee)