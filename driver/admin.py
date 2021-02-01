from django.contrib import admin
from .models import Driver,Car,Category

# Register your models here.
admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Category)