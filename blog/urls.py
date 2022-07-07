from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="index"),
    path('recette/<int:idrecette>',views.recette,name="recette"),
    path('categorie/<int:idcategorie>',views.categorie,name="categorie"),
    path('inscription',views.inscription,name="inscription"),
    path('logout',views.logout,name="logout"),
    path('login',views.login,name="login")
]