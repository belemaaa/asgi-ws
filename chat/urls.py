from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('<str:room/', views.Room.as_view()),
]