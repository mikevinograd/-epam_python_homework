from django.contrib import admin
from django.urls import include, path
from polls.views import *

app_name = 'bank'
urlpatterns = [
    path('client/create/', ClientCreateView.as_view()),
    path('wallet/create/', WalletCreateView.as_view()),
    path('client/lol/', ClientListView.as_view())
]
