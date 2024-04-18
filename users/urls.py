from django.urls import path
from .views import LoginApiView

app_name = 'users'


urlpatterns = [
  path('login/', LoginApiView.as_view(), name="login")  
]
