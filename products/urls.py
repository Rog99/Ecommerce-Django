from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BooksInfo.as_view(), name="books-page"),
    path('books/<str:tag>', views.BookTags.as_view(), name="books-tags"),
    path('gym', views.GymPage.as_view(), name="gym"),
    path('sports', views.SportsPage.as_view(), name="sports"),
    path('electronics', views.SportsPage.as_view(), name="electronics"),
]
