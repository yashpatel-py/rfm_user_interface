from unicodedata import name
from django.urls import path
from account import views

urlpatterns = [
    path('create-new-account/', views.signUp.as_view(), name="register"),
    path('login/', views.logIn.as_view(), name="login"),
    path('logout/', views.logOut.as_view(), name="logout"),
]
