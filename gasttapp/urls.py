from django.urls import path

from . import views

urlpatterns = [
    path('index/',views.index,),
    path('chidi_goods/', views.chidi_goods)
]

