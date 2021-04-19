from django.urls import path
from medicine.views import MedicineListView, MedicineCreateView, MedicineUpdateView, MedicineDeleteView

app_name = 'medicine'
urlpatterns = [
    path('', MedicineListView.as_view(), name='medicine-list'),
    path('create', MedicineCreateView.as_view(), name='medicine-create'),
    path('update/<int:pk>', MedicineUpdateView.as_view(), name='medicine-update'),
    path('delete/<int:pk>', MedicineDeleteView.as_view(), name='medicine-delete'),
    path('search', MedicineListView.as_view(), name='medicine-search')
]