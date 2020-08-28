from django.urls import path
from .views import Api_Views
app_name = "api"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('api/', Api_Views.as_view()),
]