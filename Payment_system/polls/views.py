from rest_framework import generics
from rest_framework.views import APIView
from polls.models import Wallet
from polls.serializers import WalletDetailSerializer, WalletSerializer
from rest_framework.response import Response


class WalletCreateView(generics.CreateAPIView):
    serializer_class = WalletDetailSerializer


class WalletView(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    queryset = Wallet.objects.all()


class WalletCredit(APIView):

    def post(self, request, pk, format=None):
        """
        Increase money in wallet by given amount
        """
        data = request.data
        money_raised = data["money_raised"]

        try:
            credit_result = Wallet.objects \
                .filter(pk=pk) \
                .first() \
                .credit(money_raised)
        except AssertionError as e:
            return Response(f"Error: {e}")
        except Exception as _:
            return Response("Error: Selected wallet does not exist!")

        return Response(credit_result)

    def get(self, request, pk, format=None):
        """
        Return a list of all wallets.
        """
        wallets_data = [(wallet.pk, wallet.name, wallet.money) for wallet in Wallet.objects.all()]
        request_example = {"money_raised": ""}
        return Response((wallets_data, request_example))


class WalletTransfer(APIView):

    def post(self, request, pk, format=None):
        """
        Transfer money from chosen wallet to wallet_to_send_name
        """
        data = request.data

        wallet_to_send_name = data["wallet_to_send"]
        money_to_send = data["money_to_send"]

        try:
            transfer_result = Wallet.objects \
                .filter(pk=pk) \
                .first() \
                .transfer(wallet_to_send_name, money_to_send)
        except AssertionError as e:
            return Response(f"Error: {e}")
        except Exception as _:
            return Response("Error: Selected wallet does not exist!")

        return Response(transfer_result)

    def get(self, request, pk, format=None):
        """
        Return a list of all users.
        """
        usernames = [(wallet.pk, wallet.name, wallet.money) for wallet in Wallet.objects.all()]
        request_example = {"wallet_to_send": "", "money_to_send": "100.11"}
        return Response((usernames, request_example))
