from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('login/', views.AuthorizedView.as_view(), name='login'),
    path('loginuser/', views.LoginViewdata.as_view(), name='loginuser'),
    path('lougout/', views.Lougout.as_view(), name='lougout'),
    path('signup/', views.SignUp.as_view(), name='signup'),

]
