from django.urls import path

from pms_deductions.views import deductionListView, deductionCreateView, deductionUpdateView, deductionDeleteView

app_name = 'pms_deductions'

urlpatterns = [
    path('', deductionListView.as_view(), name='deduction-List'),
    path('create', deductionCreateView.as_view(), name='deduction-create'),
    path('update/<int:pk>', deductionUpdateView.as_view(), name='deduction-update'),
    path('delete/<int:pk>', deductionDeleteView.as_view(), name='deduction-delete'),
]
