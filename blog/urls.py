from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
#comments removed from the top
