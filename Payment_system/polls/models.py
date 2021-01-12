from django.db import models, transaction
from django.db.models import F
import decimal


class Client(models.Model):
    """

    """
    db_table = "Client"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def add_wallet(self, wallet_name: str):
        Wallet(name=wallet_name, client=self).save()

    def credit(self, wallet_name: str, replenishment_amount: str):
        Wallet.objects.filter(name=wallet_name).update(money=F("money") + decimal.Decimal(replenishment_amount))

    @transaction.atomic
    def transfer_wall(self, cash_out_wallet: str, cash_in_wallet: str, replenishment_amount: str):
        if Wallet.objects.filter(name=cash_out_wallet)[0].money - decimal.Decimal(replenishment_amount) >= 0:
            Wallet.objects.filter(name=cash_out_wallet).update(money=F("money") - decimal.Decimal(replenishment_amount))
            Wallet.objects.filter(name=cash_in_wallet).update(money=F("money") + decimal.Decimal(replenishment_amount))
        else:
            print("Not enough money!")

    def __str__(self) -> str:
        return f"{self.last_name}, {self.first_name}"


class Wallet(models.Model):
    db_table = "Wallet"

    name = models.CharField(unique=True, max_length=200)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    money = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)

    def __str__(self) -> str:
        return f"{self.name}, {self.money}"


class Loglist(models.Model):
    db_table = "Loglist"

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    money_delta = models.DecimalField(default=0.00, max_digits=30, decimal_places=2)
