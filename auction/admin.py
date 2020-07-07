from django.contrib import admin

# Register your models here.
from django.contrib.auth.models import User

from .models import Product, Auction, Bid
 # Import Characters class as model



# Register the Character class in
 # admin#
 
admin.site.register(Product)
admin.site.register(Auction)
admin.site.register(Bid)