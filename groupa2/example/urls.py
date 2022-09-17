from django.urls import path
from .views import exampleView
 
urlpatterns = [
   path("", exampleView),
]