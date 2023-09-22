from django.urls import path
from .views import ClaveFavoritaApiView

urlpatterns = [
    path('crear-favorita', ClaveFavoritaApiView.as_view())
]