from django.urls import path



from .views import allowanceListView, allowanceCreateView, allowanceUpdateView, allowanceDeleteView

app_name = 'pms_allowances'

urlpatterns = [
    path('', allowanceListView.as_view(), name='allowance-List'),
    path('create', allowanceCreateView.as_view(), name='allowance-create'),
    path('update/<int:pk>', allowanceUpdateView.as_view(), name='allowance-update'),
    path('delete/<int:pk>', allowanceDeleteView.as_view(), name='allowance-delete'),
]
