from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('watch/<int:video_id>', views.watch, name='watch'),
    path('experts/', views.experts, name='experts'),
    path('recipes/', views.recipes_view, name='recipes'),
    path('recipes/<int:recipe_id>', views.recipe_view, name='recipe'),
    path('products/', views.products, name='products'),
    path('products/<int:cat>', views.categories, name='products'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('login/', views.loginpage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('profile/', views.profile, name='profile'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)