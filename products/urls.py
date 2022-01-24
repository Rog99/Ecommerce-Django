from django.urls import path
from . import views

urlpatterns = [
    path('books', views.BooksInfo.as_view(), name="books-page"),
    path('books/<str:tag>', views.BookTags.as_view(), name="books-tags"),
    path('books/<str:tag>/<int:product_id>', views.BookTags.as_view(), name="books-tags"),
    path('<str:product>', views.ProductsPage.as_view(), name="other-products"),
    path('<str:product>/<int:product_id>', views.ProductsDescriptionPage.as_view(), name="other-products")
]
