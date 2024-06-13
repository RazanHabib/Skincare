from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home_view, name="index"),
    path('signin/', views.login_view, name="login_page"),
    path('categories-list/', views.categories_list, name="cats"),
    path('new-category/', views.new_category, name="new_cat"),
    path('products-list/<int:cat>', views.products_list, name="products_list"),
    path('new-product/', views.new_product, name="new_product"),
    path('orders-list/', views.orders_list, name="orders_list"),
    path('reports/', views.reports, name="reports"),
    path('orders-list/<int:order_id>', views.order_details, name="order_details"),
    path('recipes-list/', views.recipes_list, name="recipes_list"),
    path('new-recipe/', views.new_recipe, name="new_recipe"),
    path('chatbot-list/', views.chatbot_list, name="chatbot_list"),
    path('new-chatbot/', views.new_chatbot, name="new_chatbot"),
    path('experts-list/', views.experts_list, name="experts_list"),
    path('new-expert/', views.new_expert, name="new_expert"),
    path('experts-list/<int:expert_id>', views.videos_list, name="videos_list"),
    path('new-video/<int:expert_id>', views.new_video, name="new_video"),
    path('signout/', views.logout_view, name="logout_sys"),
]