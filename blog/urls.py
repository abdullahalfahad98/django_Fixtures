from django.urls import path
from blog import views
urlpatterns = [
 
    path('', views.home),
]
# py manage.py dumpdata blog > data.json
# py manage.py loaddata blog