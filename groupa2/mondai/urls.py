from django.urls import path
from .views import mondaiListView
 
urlpatterns = [
   path("", mondaiListView),
]