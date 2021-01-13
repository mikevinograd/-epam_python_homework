from django.http import HttpResponse
from rest_framework import generics
from rest_framework.views import APIView
from polls.models import Client, Wallet
from polls.serializers import ClientDetailSerializer, WalletDetailSerializer
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# Create your views here.


class ClientCreateView(generics.CreateAPIView):
    serializer_class = ClientDetailSerializer


class WalletCreateView(generics.CreateAPIView):
    serializer_class = WalletDetailSerializer


class ClientListView(APIView):

    def post(self, request, format=None):

        data = request.data
        cash_out_wallet = data["cash_out_wallet"]
        cash_in_wallet = data["cash_in_wallet"]

        if cash_out_wallet == cash_in_wallet:
            return Response("ERROR: must put different wallets name")

        replenishment_amount = data["replenishment_amount"]
        if "-" in replenishment_amount:
            return Response("ERROR: replenishment amount must be positive")

        if Wallet.objects.filter(name=cash_in_wallet).exists() and Wallet.objects.filter(name=cash_out_wallet).exists():
            client = Wallet.objects.filter(name=cash_out_wallet)[0].client

            transfer = client.transfer_wall(cash_out_wallet, cash_in_wallet, replenishment_amount)

            return Response(transfer)
        return Response("ERROR: wallet with this name doesn't exist")

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.first_name for user in Client.objects.all()]
        request_example = {"cash_out_wallet": "", "cash_in_wallet": "", "replenishment_amount": ""}
        return Response((usernames, request_example))


class ClientСreditWallet(APIView):

    def post(self, request, format=None):

        data = request.data
        wallet_name = data["wallet_name"]
        replenishment_amount = data["replenishment_amount"]

        if "-" in replenishment_amount:
            return Response("ERROR: replenishment amount must be positive")

        if Wallet.objects.filter(name=wallet_name).exists():
            client = Wallet.objects.filter(name=wallet_name)[0].client
            credit = client.credit(wallet_name, replenishment_amount)
            return Response(credit)

        return Response("ERROR: wallet with this name doesn't exist")

    def get(self, request, format=None):
        """
        Return a list of all wallets.
        """
        walletnames = [(user.name, user.money) for user in Wallet.objects.all()]
        request_example = {"wallet_name": "", "replenishment_amount": ""}
        return Response((walletnames, request_example))
