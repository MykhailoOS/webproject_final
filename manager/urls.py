from django.urls import path, include
from .views import IndexOrderView, IndexView

app_name = 'manager'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('order/<int:pk>/', IndexOrderView.as_view(), name='approve')
]