from django.urls import path
from .views import logout_view, LoginViewUser, RegisterViewUser

app_name = 'account1'

urlpatterns = [
    path('login/', LoginViewUser.as_view(), name='login'),
    path('register/', RegisterViewUser.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
]