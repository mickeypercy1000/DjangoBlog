from zipfile import Path
from django.urls import path
from accounts.views import LoginView, RegisterView

urlpatterns = [
    path('login/', LoginView),

    path('register/', RegisterView)

]