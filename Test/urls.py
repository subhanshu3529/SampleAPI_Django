from django.urls import path
from .views import call_response
urlpatterns = [
    path('',call_response, name='call_response'),
]
