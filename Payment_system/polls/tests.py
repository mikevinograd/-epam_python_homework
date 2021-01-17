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

        decimal_money_transfer = decimal.Decimal("100.99")
        old_wallet.transfer("new_wallet", str(decimal_money_transfer))

        old_wallet_money_new: object = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_money_new = Wallet.objects.filter(name="new_wallet")[0].money

        self.assertEqual(old_wallet_money - decimal_money_transfer, old_wallet_money_new)
        self.assertEqual(new_wallet_money + decimal_money_transfer, new_wallet_money_new)


class WalletCreateViewTest(TestCase):

    def test_wallet_create(self):
        data = {
            "name": "new_wallet"
        }
        response = self.client.post(reverse('bank:create'), data)

        new_wallet = Wallet.objects.get(name="new_wallet")

        self.assertEqual(response.status_code, 201)
        self.assertEqual(new_wallet.name, 'new_wallet')


class WalletViewTest(TestCase):

    def test_get_wallet(self):
        new_wallet = Wallet.objects.create(name="new_wallet")
        response = self.client.get(reverse('bank:wallet', args=(new_wallet.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'new_wallet')


class WalletCreditViewTest(TestCase):

    def test_post_wallet_credit(self):
        new_wallet = Wallet.objects.create(name="new_wallet")
        data = {
            "money_raised": "100.99"
        }

        response = self.client.post(reverse('bank:credit', args=(new_wallet.id,)), data)
        new_wallet_money_new = Wallet.objects.filter(name="new_wallet")[0].money

        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(new_wallet_money_new), '100.99')


class WalletTransferViewTest(TestCase):

    def setUp(self):
        self.new_wallet = Wallet.objects.create(name="new_wallet")
        self.old_wallet = Wallet.objects.create(name="old_wallet")
        self.old_wallet.credit("230.99")

    def test_post_wallet_transfer(self):
        old_wallet = Wallet.objects.get(name="old_wallet")

        old_wallet_money = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_money = Wallet.objects.filter(name="new_wallet")[0].money

        decimal_transfer_amount = decimal.Decimal("100.99")
        data = {
            "wallet_to_send": "new_wallet",
            "money_to_send": f"{decimal_transfer_amount}"
        }

        response = self.client.post(reverse('bank:transfer', args=(old_wallet.id,)), data)

        old_wallet_money_new = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_money_new = Wallet.objects.filter(name="new_wallet")[0].money

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_wallet_money_new, new_wallet_money + decimal_transfer_amount)
        self.assertEqual(old_wallet_money_new, old_wallet_money - decimal_transfer_amount)

# class WalletCreditViewTest():
#
#     def test_credit_get(self):
