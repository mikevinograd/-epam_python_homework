from django.contrib import admin
from django.urls import include, path
from polls.views import *

app_name = 'bank'
urlpatterns = [
    path('wallets', WalletCreateView.as_view(), name='create'),
    path('wallets/<int:pk>/transfer/', WalletTransfer.as_view(), name='transfer'),
    path('wallets/<int:pk>/credit/', WalletCredit.as_view(), name='credit'),
    path('wallets/<int:pk>/', WalletView.as_view(), name='wallet'),
]
