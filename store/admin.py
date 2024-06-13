from django.contrib import admin
from .models import Profile, Experts, Videos, Products, Orders, Orders_items, Chatbot, Categories, Recipes

# Register your models here.
admin.site.register(Profile)
admin.site.register(Experts)
admin.site.register(Videos)
admin.site.register(Products)
admin.site.register(Orders)
admin.site.register(Orders_items)
admin.site.register(Chatbot)
admin.site.register(Categories)
admin.site.register(Recipes)
