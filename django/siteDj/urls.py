from django.urls import path
from .views import cont

urlpatterns = [
    path('', cont, name='lista')
]