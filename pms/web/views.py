from django.shortcuts import render

# Create your views here.
from apis.BillingApi import BillingApi


def index(request):
    return render(request, "layout/patient-layout.html")
