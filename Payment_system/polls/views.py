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
        print(type(request.data))

        data = request.data
        fst = data["fst"]
        snd = data["snd"]
        amount = data["money"]

        client = Wallet.objects.filter(name=fst)[0].client

        dsds = client.transfer_wall(fst, snd, amount)

        return Response(dsds)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.first_name for user in Client.objects.all()]
        return Response(usernames)
