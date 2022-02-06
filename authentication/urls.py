from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index.as_view()),
    path('about/', views.AboutPage.as_view()),
    path('sell/', views.SellerPage.as_view()),
    path('signup/', views.SignUpPage.as_view()),
    path('signin/', views.LoginPage.as_view()),
    path('logout-user/', views.logout_view),
    path('get-user/', views.get_user)
]
