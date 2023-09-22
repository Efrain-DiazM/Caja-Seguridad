from django.urls import path
from .views import LoginApiView

urlpatterns = [
    path('crear-login', LoginApiView.as_view())
]