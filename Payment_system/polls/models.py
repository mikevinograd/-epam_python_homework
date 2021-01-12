from django.db import models
from django.db.models import F
import decimal


class Client(models.Model):
    """

    """
    db_table = "Client"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def add_wallet(self, wallet_name):
        Wallet(name=wallet_name, client=self).save()

    def credit(self, wallet_name, replenishment_amount: str):
        Wallet.objects.filter(name=wallet_name).update(money=F("money") + decimal.Decimal(replenishment_amount))

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"


class Wallet(models.Model):
    db_table = "Wallet"

    name = models.CharField(unique=True, max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    money = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}, {self.money}"

    def credit_wallet(self, wallet_name, replenishment_amount):
        return Wallet(name=wallet_name, client=self.id, money=(replenishment_amount + wallet_name.money))


class Loglist(models.Model):
    db_table = "Loglist"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    money_delta = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)
