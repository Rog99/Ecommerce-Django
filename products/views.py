from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ProductTags, ProductDetails
from authentication.models import CustomUser
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

# Create your views here.
products_routes = {
    "gym": "GE",
    "sports": "SA",
    "electronics": "EE"
}

book_tags = {
    "novels": "NO",
    "inspirational": "MB",
    "defence": "DB",
    "college": "CB"
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
                    "details": details,
                    "user_id": request.user.id
                })
        except KeyError:
            return redirect("/{}".format(product))


class BooksDescriptionPage(TemplateView):
    def get(self, request, tag, product_id):
        try:
            tag = tag.split('"')[0]
            product_id = str(product_id).split('"')[0]

            # query to get the product
            book_details = ProductTags.objects\
                .filter(product=product_id, tag=book_tags[tag])\
                .select_related('product')\
                .get()

            details = {
                "id": book_details.product.id,
                "description": book_details.product.description,
                "product_name": book_details.product.product_name,
                "product_path": book_details.product.product_path,
                "price": book_details.product.price,
                "location": book_details.product.location,
                "seller_id": book_details.product.user_id
            }
            return render(request, "pages/product_description.html", {
                "details": details,
                "user_id": request.user.id
            })

        except ProductTags.DoesNotExist:
            return redirect("/{}".format(tag))

        except KeyError:
            return redirect("/{}".format(tag))


class ManageProducts(TemplateView):
    def get(self, request):
        # user = CustomUser.objects.filter(id=request.user.id).get()
        # print(user)
        products = ProductDetails.objects.filter(user=request.user).values()
        print(products)
        return render(request, 'pages/manage_products.html', {
            'products': products
        })
