from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import CustomUser

# Create your views here.


class Index(TemplateView):
    def get(self, request):
        return render(request, "pages/home.html")


class AboutPage(TemplateView):
    def get(self, request):
        return render(request, "pages/about.html")


class SellerPage(TemplateView):
    def get(self, request):
        return render(request, "pages/sell.html")


class SignUpPage(TemplateView):
    def get(self, request):
        return render(request, "pages/signup.html")

    def post(self, request):
        if request.POST["password"] == request.POST["confirm_password"]:
            print("reached here")
            data = request.POST
            user = CustomUser(
                email=data["email"],
                full_name=data["full_name"],
                phone_number=data["phone_number"]
            )
            user.set_password(data["password"])
            user.save()
            return redirect('/')

        else:
            return redirect('/signup')


# class