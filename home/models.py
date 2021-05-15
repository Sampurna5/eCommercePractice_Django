from django.db import models
from django.urls import reverse

LABEL = (('new', 'new'), ('hot', 'hot'), ('', 'default'))
STATUS = (('active', 'active'), ('', 'default'))
STOCK = (('in', 'In Stock'), ('out', 'Out of Stock'))


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_category_slug(self):
        return reverse('home:category', kwargs={'slug': self.id})


class Item(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=250, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    discounted_price = models.IntegerField()
    description = models.TextField(blank=True)
    label = models.CharField(max_length=50, choices=LABEL, blank=True)
    status = models.CharField(max_length=50, choices=STATUS, blank=True)
    stock = models.CharField(max_length=50, choices=STOCK)

    def __str__(self):
        return self.title

    def get_item_slug(self):
        return reverse('home:product', kwargs={'slug': self.slug})

    def get_cart_slug(self):
        return reverse('home:add-to-cart', kwargs={'slug': self.slug})

    def get_wishlist_slug(self):
        return reverse('home:add-to-wishlist', kwargs={'slug': self.slug})


class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    text = models.TextField()
    rank = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS, blank=True)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Ad(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.subject


class Cart(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=250)
    quantity = models.IntegerField(default=1)
    user = models.CharField(max_length=200)
    date = models.DateTimeField(null=True)
    total = models.IntegerField()

    def delete_cart_slug(self):
        return reverse('home:delete-cart', kwargs={'slug': self.slug})

    def add_single_item_cart_slug(self):
        return reverse('home:add-single-item-cart', kwargs={'slug': self.slug})

    def remove_single_item_cart_slug(self):
        return reverse('home:remove-single-item-cart', kwargs={'slug': self.slug})

    def __str__(self):
        return self.user


class Wishlist(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=250)
    user = models.CharField(max_length=200)

    def delete_wishlist_slug(self):
        return reverse('home:delete-wishlist-item', kwargs={'slug': self.slug})


