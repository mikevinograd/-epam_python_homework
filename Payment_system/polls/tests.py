from django.test import TestCase
from django.urls import reverse
from polls.models import Wallet
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

    def test_incorrect_credit_value(self):
        new_wallet = Wallet.objects.get(name="new_wallet")
        with self.assertRaisesMessage(AssertionError, "Incorrect credit value"):
            new_wallet.credit("-100.99")

    def test_transfer(self):
        """
        Take two wallets, old wallet has money on balance,
        transfer some money from old wallet to new wallet.
        Check the balance of two wallets.
        """
        old_wallet = Wallet.objects.get(name="old_wallet")

        old_wallet_money = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_money = Wallet.objects.filter(name="new_wallet")[0].money

        decimal_money_transfer = decimal.Decimal("100.99")
        old_wallet.transfer("new_wallet", str(decimal_money_transfer))

        old_wallet_money_new: object = Wallet.objects.filter(name="old_wallet")[0].money
        new_wallet_money_new = Wallet.objects.filter(name="new_wallet")[0].money

        self.assertEqual(old_wallet_money - decimal_money_transfer, old_wallet_money_new)
        self.assertEqual(new_wallet_money + decimal_money_transfer, new_wallet_money_new)

    def test_not_exist_wallet_name_transfer(self):
        old_wallet = Wallet.objects.get(name="old_wallet")
        with self.assertRaisesMessage(AssertionError, "Receiver doest not exist!"):
            old_wallet.transfer("nonexistent_name", "10.99")

    def test_sender_is_receiver_wallet_name_transfer(self):
        old_wallet = Wallet.objects.get(name="old_wallet")
        with self.assertRaisesMessage(AssertionError, "Sender must not be receiver!"):
            old_wallet.transfer("old_wallet", "10.99")

    def test_incorrect_transfer_value(self):
        old_wallet = Wallet.objects.get(name="old_wallet")
        with self.assertRaisesMessage(AssertionError, "Incorrect transfer value!"):
            old_wallet.transfer("new_wallet", "-10.99")

    def test_not_enough_money_for_transfer(self):
        new_wallet = Wallet.objects.get(name="new_wallet")
        with self.assertRaisesMessage(AssertionError, "Not enough money!"):
            new_wallet.transfer("old_wallet", "10.99")


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

    def setUp(self):
        self.new_wallet = Wallet.objects.create(name="new_wallet")

    def test_get_wallet_credit(self):
        new_wallet = Wallet.objects.get(name="new_wallet")

        response = self.client.get(reverse('bank:credit', args=(new_wallet.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0][0][1], 'new_wallet')

    def test_post_wallet_credit(self):
        new_wallet = Wallet.objects.get(name="new_wallet")
        new_wallet_money = Wallet.objects.filter(name="new_wallet")[0].money

        decimal_money_transfer = decimal.Decimal("100.99")
        data = {
            "money_raised": f"{decimal_money_transfer}"
        }

        response = self.client.post(reverse('bank:credit', args=(new_wallet.id,)), data)
        new_wallet_money_new = Wallet.objects.filter(name="new_wallet")[0].money

        self.assertEqual(response.status_code, 200)
        self.assertEqual(new_wallet_money_new, new_wallet_money + decimal_money_transfer)

    def test_post_incorrect_money_amount_credit(self):
        new_wallet = Wallet.objects.get(name="new_wallet")
        decimal_money_transfer = decimal.Decimal("-100.99")
        data = {
            "money_raised": f"{decimal_money_transfer}"
        }

        response = self.client.post(reverse('bank:credit', args=(new_wallet.id,)), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Error: Incorrect credit value")

    def test_post_incorrect_wallet_name_credit(self):
        decimal_money_transfer = decimal.Decimal("-100.99")
        data = {
            "money_raised": f"{decimal_money_transfer}"
        }
        incorrect_id = 0
        response = self.client.post(reverse('bank:credit', args=(incorrect_id,)), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Error: Selected wallet does not exist!")


class WalletTransferViewTest(TestCase):

    def setUp(self):
        self.new_wallet = Wallet.objects.create(name="new_wallet")
        self.old_wallet = Wallet.objects.create(name="old_wallet")
        self.old_wallet.credit("230.99")

    def test_get_wallet_transfer(self):
        new_wallet = Wallet.objects.get(name="new_wallet")

        response = self.client.get(reverse('bank:transfer', args=(new_wallet.id,)))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0][0][1], 'new_wallet')

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

    def test_post_incorrect_money_amount_transfer(self):
        old_wallet = Wallet.objects.get(name="old_wallet")

        decimal_transfer_amount = decimal.Decimal("-100.99")
        data = {
            "wallet_to_send": "new_wallet",
            "money_to_send": f"{decimal_transfer_amount}"
        }

        response = self.client.post(reverse('bank:transfer', args=(old_wallet.id,)), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Error: Incorrect transfer value!")

    def test_post_incorrect_wallet_name_transfer(self):
        decimal_transfer_amount = decimal.Decimal("-100.99")
        data = {
            "wallet_to_send": "new_wallet",
            "money_to_send": f"{decimal_transfer_amount}"
        }
        incorrect_id = 0
        response = self.client.post(reverse('bank:transfer', args=(incorrect_id,)), data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, "Error: Selected wallet does not exist!")
