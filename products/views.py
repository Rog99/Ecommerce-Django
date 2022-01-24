from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProductTags, ProductDetails

# Create your views here.
products_routes = {
    "gym": "GE",
    "sports": "SA",
    "electronics": "EE"
}


class BooksInfo(TemplateView):
    def get(self, request):
        return render(request, "pages/books.html")


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


class ProductsPage(TemplateView):
    def get(self, request, product):
        try:
            items = ProductDetails.objects.filter(product_type=products_routes[product]).values(
                'id', 'product_name', 'product_path', 'price', 'description'
            )
            return render(request, "pages/products.html", {
                "cards": items,
                "product": product
            })
        except KeyError:
            return redirect("/")


class ProductsDescriptionPage(TemplateView):
    def get(self, request, product, product_id):
        try:
            details = ProductDetails.objects.filter(id=product_id, product_type=products_routes[product]).values(
                'id', 'product_name', 'product_path', 'price', 'description', 'location', 'user_id'
            ).first()
            if not bool(details):
                return redirect("/{}".format(product))
            else:
                return render(request, "pages/product_description.html", {
                    "details": details
                })
        except KeyError:
            return redirect("/{}".format(product))
