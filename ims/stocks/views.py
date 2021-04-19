from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView

from django.db.models import Q
from stocks.models import Stocks
from purchases.models import Purchases
from newSales.models import NewSales
from items.models import Items
    
class StocksListView(ListView):
    model = Stocks
    template_name = "stocks/stocks-list.html"
    def get_queryset(self):
        stk = []
        object_list = Items.objects.all()
        for object in object_list:
            sId = object.id
            sCode= object.code
            sDescription= object.description
            sQuantity = object.purchase
            try:
                prch = Purchases.objects.get(Q(pCode = object.code))
                prchQuan = prch.pQuantity
            except Purchases.DoesNotExist:
                prchQuan = 0
            try:
                sales = NewSales.objects.get(Q(code = object.code))
                salesQuan = sales.quantity
            except NewSales.DoesNotExist:
                salesQuan = 0
            quan = int(sQuantity) + int(prchQuan) - int(salesQuan)
            if int(quan) >= 50:
                sRStatus = "Available"
            elif int(quan) > 0 and int(quan) < 50:
                sRStatus = "Limited Stocks"
            else:
                sRStatus = "Out of Stocks"
            stk.append({'id': sId,'code': sCode, 'description': sDescription, 'purchase': quan, 'sRStatus': sRStatus
            })
        return stk

