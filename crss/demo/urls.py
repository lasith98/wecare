from django.urls import path

from demo.views import DemoListView, DemoCreateView, DemoUpdateView, DemoDeleteView

app_name = 'demo'
urlpatterns = [
    path('', DemoListView.as_view(), name='demo-list'),
    path('create', DemoCreateView.as_view(), name='demo-create'),
    path('update/<int:pk>', DemoUpdateView.as_view(), name='demo-update'),
    path('delete/<int:pk>', DemoDeleteView.as_view(), name='demo-delete'),
]
