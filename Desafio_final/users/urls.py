from django.urls import path, index
from users.views import login_request 

urlpatterns = [
    path("login/", login_request, name = "login")
    
]