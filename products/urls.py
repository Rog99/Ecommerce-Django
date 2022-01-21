from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BooksInfo.as_view(), name="books-page"),
    path('books/inspirational', views.MotivationalBooks.as_view(), name="books-motivation"),
    path('books/defence', views.DefenceBooks.as_view(), name="books-motivation"),
    path('books/novels', views.Novels.as_view(), name="books-novels"),
    path('gym', views.GymPage.as_view(), name="gym"),
    path('sports', views.SportsPage.as_view(), name="sports"),
    path('electronics', views.SportsPage.as_view(), name="electronics"),
]
