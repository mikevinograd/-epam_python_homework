from rest_framework import serializers
from bank.models import Wallet


class WalletDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("name",)


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"
