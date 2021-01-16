from django.db import models, transaction
from django.db.models import F
import decimal


class Wallet(models.Model):
    db_table = "Wallet"
    name = models.CharField(unique=True, max_length=200)
    money = models.DecimalField(default=0.00, max_digits=30, decimal_places=2, editable=True)

    def credit(self, money_raised: str):
        """
        Increase money in wallet by given amount
        :param money_raised: "str"
        :return: "OK"
        """

        raise_money_decimal = decimal.Decimal(money_raised)

        if not (raise_money_decimal > 0):
            raise AssertionError("Incorrect credit value")

        Wallet.objects.filter(name=self.name).update(money=F("money") + raise_money_decimal)

        return "OK"

    def transfer(self, wallet_to_send_name: str, money_to_send: str):
        """
        Transfer money from chosen wallet to wallet_to_send_name
        :param wallet_to_send_name: str
        :param money_to_send: str
        :return: "OK"
        """

        money_to_send_decimal = decimal.Decimal(money_to_send)

        if not Wallet.objects.filter(name=wallet_to_send_name).exists():
            raise AssertionError("Receiver doest not exist!")

        if wallet_to_send_name == self.name:
            raise AssertionError("Sender must not be receiver!")

        if not (money_to_send_decimal > 0):
            raise AssertionError("Incorrect transfer value")

        with transaction.atomic():
            is_changed = Wallet.objects \
                .filter(name=self.name, money__gte=money_to_send_decimal) \
                .update(money=F("money") - money_to_send_decimal)  # Check if it is enough money  on the wallet
            # and subtracts the amount of money from wallet. True if action was done, False if doesn't

            if is_changed:
                Wallet.objects \
                    .filter(name=wallet_to_send_name) \
                    .update(money=F("money") + money_to_send_decimal)  # Increase money amount in wallet to transfer
            else:
                raise AssertionError("Not enough money!")

        return "OK"

    def __str__(self) -> str:
        """
        Return wallet name, and wallet balance
        :return: str
        """

        return f"{self.name}, {self.money}"
