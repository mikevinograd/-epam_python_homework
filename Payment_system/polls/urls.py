from django.contrib import admin
from django.urls import include, path
from polls.views import *

app_name = 'bank'
urlpatterns = [
    path('client/create/', ClientCreateView.as_view()),
    path('wallet/create/', WalletCreateView.as_view()),
    path('client/transfer/', ClientListView.as_view()),
    path('client/credit/', ClientСreditWallet.as_view())
]
