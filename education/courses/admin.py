from django.contrib import admin

from .models import Lesson, Product, UserAvailableProduct, UserProgress

admin.site.register(Lesson)
admin.site.register(UserAvailableProduct)
admin.site.register(Product)
admin.site.register(UserProgress)
