from django.urls import path, include
from . import views

app_name = "shift_management_system"

urlpatterns = [
    path('next_month_shift' , views.genarate_next_month_shift , name = "genarate_next_month_shift"),
    path('view_shifts' , views.view_shifts , name = "view_shifts"),
]