from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProductTags

# Create your views here.


class BooksInfo(TemplateView):
    def get(self, request):
        return render(request, "pages/books.html")


class GymPage(TemplateView):
    def get(self, request):
        return render(request, "pages/gym.html")


class SportsPage(TemplateView):
    def get(self, request):
        return render(request, "pages/sports.html")


class ElectronicsPage(TemplateView):
    def get(self, request):
        return render(request, "pages/electronics.html")


class MotivationalBooks(TemplateView):
    def get(self, request):
        book_tags = ProductTags.get_books_by_tags('MB')

        card2 = {
            "bookName": "Inspirational Books",
            "price": 100,
            "bookSummary": "Roberts story of growing up with two dads one of the best books if you are interested in money",
            "imagePath": "RDPD.jpg"
        }
        card3 = {
            "bookName": "Inspirational Books",
            "price": 100,
            "bookSummary": "Book written by the most inspiring woman",
            "imagePath": "becoming.jpg"
        }
        card4 = {
            "bookName": "Inspirational Books",
            "price": 120,
            "bookSummary": "Is a business and self-help book written by Stephen R. Covey",
            "imagePath": "7habits.jpg"
        }
        return render(request, "pages/books/inspirational.html", {
            "cards": book_tags
        })


class DefenceBooks(TemplateView):
    def get(self, request):
        card1 = {
            "bookName": "Competitive Books",
            "price": 395,
            "bookSummary": "Best book for NDA aspirants 8000+ MCQ practise questions.",
            "imagePath": "Bookpathfinder.jpg"
        }
        card2 = {
            "bookName": "Competitive Books",
            "price": 300,
            "bookSummary": "Best books for CDS aspirants. 8000+ MCQS practise questions.",
            "imagePath": "Bookpathfinder.jpg"
        }
        book_tags = ProductTags.get_books_by_tags('DB')
        return render(request, "pages/books/defence.html", {
            "cards": book_tags
        })


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

            return render(request, "pages/books/defence.html", {
                "cards": book_tags
            })

        else:
            redirect('/books')


class Novels(TemplateView):
    def get(self, request):
        book1 = {
            "bookName": "Five Feet Apart",
            "price": 120,
            "imagePath": "novel1.jpg"
        }
        book2 = {
            "bookName": "Green and Black Flowers",
            "price": 44,
            "imagePath": "novel2.jpg"
        }
        book3 = {
            "bookName": "Black Dots",
            "price": 44,
            "imagePath": "novel3.jpg"
        }
        book_tags = ProductTags.get_books_by_tags('NO')
        book4 = {
            "bookName": "Red Flowy",
            "price": 44,
            "imagePath": "novel4.jpg"
        }
        return render(request, 'pages/books/novels.html', {
            "cards": book_tags
        })
