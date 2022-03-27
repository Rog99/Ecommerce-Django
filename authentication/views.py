from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.db.utils import IntegrityError
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from products.middlewares import check_user_login
from products.models import ProductDetails, ProductTags
import time
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from random import random
import json

# Create your views here.


class Index(TemplateView):
    def get(self, request):
        user = request.user
        return render(request, "pages/home.html", {"user": user})


class AboutPage(TemplateView):
    def get(self, request):
        return render(request, "pages/about.html")


# This function generates a random file name to avoid duplicates in image uploads
def random_file_name(file_name: str) -> str:
    file_extensions_arr = file_name.split('.')
    random_str = str(time.time()*random()).replace('.', '_')
    return "{}.{}".format(random_str, file_extensions_arr[len(file_extensions_arr)-1])


class SellerPage(TemplateView):
    @method_decorator(check_user_login)
    def get(self, request):
        return render(request, "pages/sell.html")

    def post(self, request):
        product_name = request.POST["product_name"]
        product_path = request.FILES["product_path"]
        product_type = request.POST['product_type']
        price = request.POST["price"]
        description = request.POST["description"]
        location = request.POST["location"]
        user = request.user

        fs = FileSystemStorage()
        file_unique_name = random_file_name(product_path.name)
        fs.save(file_unique_name, product_path)
        sell = ProductDetails(
            product_name=product_name,
            product_path=file_unique_name,
            product_type=product_type,
            price=int(price),
            description=description,
            location=location,
            user=user
        )

        try:
            sell.save()
            if product_type == "BK":
                tag = ProductTags(product=sell, tag=request.POST["book_type"])
                tag.save()

            print(sell.id)
            messages.info(request, "Product uploaded successfully")
            return redirect('/')

        except ValueError:
            messages.error(request, "Error in saving data to the database")
            return redirect('/sell')


class SignUpPage(TemplateView):
    def get(self, request):
        return render(request, "pages/signup.html")

    def post(self, request):
        if request.POST["password"] == request.POST["confirm_password"]:
            data = request.POST
            user = CustomUser(
                email=data["email"],
                full_name=data["full_name"],
                phone_number=data["phone_number"]
            )
            user.set_password(data["password"])
            try:
                user.save()
                return redirect('/signin')

            except IntegrityError:
                messages.error(request, "User already exits. Try using a different email address")
                return redirect('/signup')

        else:
            messages.error(request, "Passwords dosen't match")
            return redirect('/signup')


class LoginPage(TemplateView):
    def get(self, request):
        return render(request, 'pages/signin.html')

    def post(self, request):
        email = request.POST["email"]
        password = request.POST["password"]
        try:
            user = CustomUser.objects.get(email=email)

            if user is not None:

                if user.check_password(password):
                    login(request, user)
                    return redirect('/')

                else:
                    messages.error(request, "Wrong user credentials. Try again")
                    return redirect('/signin')


            else:
                messages.info("Wrong user credentials. Try again")
                return redirect('/signin')

        except CustomUser.DoesNotExist:
            messages.info(request, "User does not exist.")
            return redirect('/signin')


def logout_view(request):
    logout(request)
    return redirect("/signin")


def get_user(request):
    # try:
    json_object = json.dumps({"user_id": request.user.id}, indent=4).encode('utf-8')
    print(json_object)
    return HttpResponse(json_object, content_type='application/json')

    # except TypeError:
    #     return redirect('/signin')
