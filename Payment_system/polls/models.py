from django.db import models


class Client(models.Model):
    """

    """
    db_table = "Client"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def add_wallet(self, wallet_name):
        return Wallet(name=wallet_name, client=self.id)

    # def credit(self, wallet_name, replenishment_amount):
    #     return Wallet(name=wallet_name, client=self.id)

    def __str__(self) -> str:
        return f"self.last_name, self.first_name"


class Wallet(models.Model):
    db_table = "Wallet"

    name = models.CharField(unique=True, max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    money = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)

    def __str__(self) -> str:
        return f"self.name, self.money"


class Loglist(models.Model):
    db_table = "Loglist"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    money_delta = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)
