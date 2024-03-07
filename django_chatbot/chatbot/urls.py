from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('chatbot',views.chatbot,name='chatbot'),
    path('',views.login,name='login'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
]
