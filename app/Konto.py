class Konto:

    def przelew_wychodzacy(self,kwota):
        if self.saldo >= kwota and kwota > 0:
            self.saldo -= kwota
    def przelew_przychodzacy(self, kwota):
        if kwota > 0:
            self.saldo += kwota
