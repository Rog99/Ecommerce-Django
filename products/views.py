from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProductTags, ProductDetails

# Create your views here.


class BooksInfo(TemplateView):
    def get(self, request):
        return render(request, "pages/books.html")


class GymPage(TemplateView):
    def get(self, request):
        items = ProductDetails.objects.filter(product_type="GE").values(
            'id', 'product_name', 'product_path', 'price', 'description'
        )
        return render(request, "pages/gym.html", {
            "cards": items
        })


class SportsPage(TemplateView):
    def get(self, request):
        return render(request, "pages/sports.html")


class ElectronicsPage(TemplateView):
    def get(self, request):
        return render(request, "pages/electronics.html")


class BookTags(TemplateView):
    def get(self, request, tag):
        if tag == "inspirational" or tag == "defence" or tag == "novels" or tag == "college":
            if tag == "inspirational":
                book_tags = ProductTags.get_books_by_tags('MB')
            elif tag == "defence":
                book_tags = ProductTags.get_books_by_tags('DB')
            elif tag == "novels":
                book_tags = ProductTags.get_books_by_tags('NO')
            else:
                book_tags = ProductTags.get_books_by_tags('CB')

            return render(request, "pages/tags.html", {
                "cards": book_tags
            })

        else:
            redirect('/books')
