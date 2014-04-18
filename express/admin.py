from express.models import UserLogin
from django.contrib import admin
from express.models import Product, Service, Client, Aed, Battery, Eyewash
# Register your models here.

admin.site.register(UserLogin)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Client)
admin.site.register(Aed)
admin.site.register(Battery)
admin.site.register(Eyewash)
