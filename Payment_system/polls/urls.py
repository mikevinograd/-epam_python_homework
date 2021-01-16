from django.contrib import admin
from django.urls import include, path
from polls.views import *

app_name = 'bank'
urlpatterns = [
    path('wallets', WalletCreateView.as_view()),
    path('wallets/<int:pk>/transfer/', WalletTransfer.as_view()),
    path('wallets/<int:pk>/credit/', WalletCredit.as_view()),
    path('wallets/<int:pk>/', WalletView.as_view()),
]
