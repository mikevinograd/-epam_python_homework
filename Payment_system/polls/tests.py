from django.test import TestCase
from django.urls import reverse
from polls.models import Wallet
from polls.views import WalletCreateView, WalletView, WalletTransfer, WalletCredit
import decimal


class WalletModelTests(TestCase):

    def setUp(self):
        self.new_wallet = Wallet.objects.create(name="new_wallet")
        self.old_wallet = Wallet.objects.create(name="old_wallet")
        self.old_wallet.credit("230.99")

    def test_credit(self):
        """
        Take wallet and increase money balance.
        Check it after.
        """
        new_wallet = Wallet.objects.get(name="new_wallet")
        new_wallet.credit("100.99")
        new_wallet_money = Wallet.objects.filter(name="new_wallet")[0].money
        decimal_money_raised = decimal.Decimal("100.99")
        self.assertEqual(new_wallet_money, decimal_money_raised)

    def test_transfer(self):
        """
        Take two wallets, old wallet has money on balance,
        transfer some money from old wallet to new wallet.
        Check the balance of two wallets.
        """
        old_wallet = Wallet.objects.get(name="old_wallet")
        new_wallet = Wallet.objects.get(name="new_wallet")

        old_wallet_money = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_money = Wallet.objects.filter(name="new_wallet")[0].money

        old_wallet.transfer("new_wallet", "100.99")

        decimal_money_transfer = decimal.Decimal("100.99")

        old_wallet_transferred_money = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_transferred_money = Wallet.objects.filter(name="new_wallet")[0].money

        self.assertEqual(old_wallet_money - decimal_money_transfer, old_wallet_transferred_money)
        self.assertEqual(new_wallet_money + decimal_money_transfer, new_wallet_transferred_money)


class WalletViewTest(TestCase):

    def test_get_wallet(self):
        Wallet.objects.create(name="new_wallet")
        response = self.client.get(reverse('wallets:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(
            response.context['name'],
            ['<Question: Past question.>']
        )

# class WalletCreditViewTest():
#
#     def test_credit_get(self):
