from django.shortcuts import render
from django.views.generic import TemplateView

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
        card1 = {
            "bookName": "Inspirational Books",
            "price": 120,
            "bookSummary": "One fo the highest selling books written by a man with zero haters",
            "imagePath": "book.jpg"
        }
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
            "cards": [card1, card2, card3, card4]
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
        return render(request, "pages/books/defence.html", {
            "cards": [card1, card2]
        })


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
        book4 = {
            "bookName": "Red Flowy",
            "price": 44,
            "imagePath": "novel4.jpg"
        }
        return render(request, 'pages/books/novels.html', {
            "cards": [book1, book2, book3, book4]
        })
