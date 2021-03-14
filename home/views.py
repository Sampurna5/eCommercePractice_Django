from django.shortcuts import render
from django.views.generic import View
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
