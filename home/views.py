from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib import messages, auth
from .models import *


# Create your views here.
class BaseView(View):
    view = {}


class HomeView(BaseView):
    def get(self, request):
        self.view['categories'] = Category.objects.all()
        self.view['sliders'] = Slider.objects.all()
        self.view['items'] = Item.objects.all()
        self.view['brands'] = Brand.objects.all()
        self.view['hot'] = Item.objects.filter(label='hot')
        self.view['new'] = Item.objects.filter(label='new')
        self.view['ad_1'] = Ad.objects.filter(rank=1)
        self.view['ad_2'] = Ad.objects.filter(rank=2)
        self.view['ad_3'] = Ad.objects.filter(rank=3)
        self.view['ad_4'] = Ad.objects.filter(rank=4)
        self.view['ad_5'] = Ad.objects.filter(rank=5)
        self.view['ad_6'] = Ad.objects.filter(rank=6)

        return render(request, 'index.html', self.view)


class ItemDetailView(BaseView):
    def get(self, request, slug):
        self.view['product_details'] = Item.objects.filter(slug=slug)

        return render(request, 'product-detail.html', self.view)


class CategoryItemView(BaseView):
    def get(self, request, slug):
        self.view['category_products'] = Item.objects.filter(category=slug)

        return render(request, 'product-list.html', self.view)


class SearchView(BaseView):
    def get(self, request):
        if request.method == 'GET':
            search = request.GET['search']
            self.view['search_products'] = Item.objects.filter(
                title__icontains=search
            )
            self.view['search_for'] = search
        else:
            return redirect('/')

        return render(request, 'search-list.html', self.view)


def signup(request):
    if request.method == 'post':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']

        if password == re_password:
            for character in first_name:
                if character.isdigit():
                    messages.error(request, 'Name cannot have number!!')
                    return redirect("home:signup")
            for character in last_name:
                if character.isdigit():
                    messages.error(request, 'Name cannot have number!!')
                    return redirect("home:signup")
            if len(password) < 8:
                messages.error(request, 'Password length must exceed 8 characters!!')
                return redirect("home:signup")
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!!')
                return redirect('home:signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered!!')
                return redirect('home:signup')
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    username=username,
                    password=password
                )
                user.save()

                messages.success(request, 'Account created successfully!!')
                return redirect('home:signup')
        else:
            messages.error(request, 'Password does not match!!')

    return render(request, 'login.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid email/username or password!!')
            return redirect('home:login')

    return render(request, 'login.html')
