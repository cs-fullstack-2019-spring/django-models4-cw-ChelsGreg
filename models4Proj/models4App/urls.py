from django.urls import path

from . import views

urlpatterns =[
    path('children/', views.allChild, name ='children'),
    path('moms/', views.momChild, name="moms"),
    # path('addchild/', views.addChild, name="add"),
    path('deletemom/', views.deleteMom, name="delete"),
    path("", views.index, name="index"),

]


