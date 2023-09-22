from django.urls import path
from .views import LoginApiView, IdentificacionApiView

urlpatterns = [
    path('crear-login', LoginApiView.as_view()),
    path('crear-identificacion', LoginApiView.as_view()),
]