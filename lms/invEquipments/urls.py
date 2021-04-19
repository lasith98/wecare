from django.urls import path
from invEquipments.views import InvEquipmentsListView, InvEquipmentsCreateView, InvEquipmentsUpdateView, InvEquipmentsDeleteView, request

app_name = 'invEquipments'
urlpatterns = [
    path('', InvEquipmentsListView.as_view(), name='invEquipments-list'),
    path('create', InvEquipmentsCreateView.as_view(), name='invEquipments-create'),
    path('update/<int:pk>', InvEquipmentsUpdateView.as_view(), name='invEquipments-update'),
    path('delete/<int:pk>', InvEquipmentsDeleteView.as_view(), name='invEquipments-delete'),
    path('search', InvEquipmentsListView.as_view(), name='invEquipments-search'),
    path('request/<int:pk>', request, name='invEquipments-request')
]