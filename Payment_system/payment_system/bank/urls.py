from django.urls import path
from payment_system.bank.views import *

app_name = 'bank'
urlpatterns = [
    path('wallets/', WalletCreateView.as_view(), name='create_wallet'),
    path('wallets/<int:pk>/', WalletView.as_view(), name='get_wallet'),
    path('wallets/<int:pk>/credit/', WalletCredit.as_view(), name='credit'),
    path('wallets/<int:pk>/transfer/', WalletTransfer.as_view(), name='transfer')
]
