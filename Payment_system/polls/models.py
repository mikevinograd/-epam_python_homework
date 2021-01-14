from django.db import models, transaction
from django.db.models import F
import decimal



# class Loglist(models.Model):
#     db_table = "Loglist"
#
#     client = models.ForeignKey(Client, on_delete=models.CASCADE)


class Wallet(models.Model):
    db_table = "Wallet"
    name = models.CharField(unique=True, max_length=200)
    money = models.DecimalField(default=0.00, max_digits=30, decimal_places=2, editable=True)

    def credit(self, replenishment_amount: str):
        """
        Increase money in wallet by given among
        :param replenishment_amount: str
        :return:
        """
        print(self, type(self.name), Wallet.objects.filter(name=self.name))
        Wallet.objects.filter(name=self.name).update(money=F("money") + decimal.Decimal(replenishment_amount))
        # self.update(money=F("money") + decimal.Decimal(replenishment_amount))


    @transaction.atomic
    def transfer_wall(self, cash_in_wallet: str, replenishment_amount: str):
        """
        Transfer money from cash_out_wallet to cash_in_wallet
        :param cash_in_wallet: str
        :param replenishment_amount: str
        :return:
        """
        if Wallet.objects.filter(name=self.name)[0].money - decimal.Decimal(replenishment_amount) >= 0:
            Wallet.objects.filter(name=self.name).update(money=F("money") - decimal.Decimal(replenishment_amount))
            Wallet.objects.filter(name=cash_in_wallet).update(money=F("money") + decimal.Decimal(replenishment_amount))
        else:
            print("Not enough money!")


    def __str__(self) -> str:
        return f"{self.name}, {self.money}"
