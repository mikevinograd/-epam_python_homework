from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from polls.models import Wallet
from polls.serializers import WalletDetailSerializer, WalletSerializer
from rest_framework.response import Response
from django.core.exceptions import ValidationError


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.


class WalletCreateView(generics.CreateAPIView):
    serializer_class = WalletDetailSerializer


class WalletView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class WalletTransfer(APIView):

    def post(self, request, format=None):

        data = request.data
        cash_out_wallet = data["cash_out_wallet"]
        cash_in_wallet = data["cash_in_wallet"]

        if cash_out_wallet == cash_in_wallet:
            raise ValidationError("ERROR: must put different wallets name")

        replenishment_amount = data["replenishment_amount"]
        if "-" in replenishment_amount:
            raise ValidationError("ERROR: replenishment amount must be positive")

        if Wallet.objects.filter(name=cash_in_wallet).exists() and Wallet.objects.filter(name=cash_out_wallet).exists():
            # client = Wallet.objects.filter(name=cash_out_wallet)[0].client

            transfer = Wallet.objects.filter(name=cash_out_wallet).transfer_wall(cash_out_wallet, cash_in_wallet,
                                                                                 replenishment_amount)

            return Response(transfer)
        raise ValidationError("ERROR: wallet with this name doesn't exist")

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [wallet.name for wallet in Wallet.objects.all()]
        request_example = {"cash_out_wallet": "", "cash_in_wallet": "", "replenishment_amount": ""}
        return Response((usernames, request_example))


class WalletCredit(APIView):

    def post(self, request, format=None):

        data = request.data
        wallet_name = data["wallet_name"]
        replenishment_amount = data["replenishment_amount"]

        if "-" in replenishment_amount:
            raise ValidationError("ERROR: replenishment amount must be positive")

        if Wallet.objects.filter(name=wallet_name).exists():
            # client = Wallet.objects.filter(name=wallet_name)[0].client
            credit = Wallet.objects.filter(name=wallet_name).credit(replenishment_amount)
            return Response(credit)

        raise ValidationError("ERROR: wallet with this name doesn't exist")

    def get(self, request, format=None):
        """
        Return a list of all wallets.
        """
        walletnames = [(user.name, user.money) for user in Wallet.objects.all()]
        request_example = {"wallet_name": "", "replenishment_amount": ""}
        return Response((walletnames, request_example))
