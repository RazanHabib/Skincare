from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.core.mail import EmailMessage
import requests, json, random
from .models import Videos, Products, Orders, Orders_items, Profile, Chatbot, User, Categories, Recipes
from django.forms.models import model_to_dict
from django.db.models import Q
from django.contrib.auth import logout, login, authenticate

# Create your views here.
def home(request):
    videos = Videos.objects.all().order_by('-id')[0:4]
    first = videos[0] or None
    user = request.user.is_authenticated

    products = Products.objects.all().order_by('-id')[0:10]

    if request.method == 'POST':
        name = request.POST["name"]
        subject = "Beaty Shop: From " + name + " - " + request.POST["subject"]
        email = request.POST["email"]
        message = request.POST["message"]
        if subject and message and email:
            try:
                msg = EmailMessage(subject, message, "razan.alfulaiti@gmail.com", ["razan.alfulaiti@gmail.com"])
                msg.send()
            except Exception as err:
                return render(request, 'home.html', {'videos': videos, 'firstVid': first, 'products': products, "user": user , 'send_error': True})
            return HttpResponseRedirect("thankyou/")
        
    return render(request, 'home.html', {'videos': videos, 'firstVid': first, 'products': products, "user": user})

def categories(request, cat):
    category = Categories.objects.filter(id=cat).get()

    products = Products.objects.filter(category=category).order_by('-id')

    return render(request, 'products.html', { 'products': products, 'category': category })

def recipes_view(request):
    recipes = Recipes.objects.all()

    return render(request, 'recipes.html', { 'recipes': recipes })

def recipe_view(request, recipe_id):
    recipe = Recipes.objects.filter(id=recipe_id).get()

    return render(request, 'recipe.html', { 'recipe': recipe })

def products(request):
    products = Products.objects.all().order_by('-id')

    return render(request, 'products.html', { 'products': products })


def chatbot(request):
    if request.method == 'POST':
        question = request.POST["question"]
        answer = Chatbot.objects.filter(Q(question__contains=question) | Q(answer__contains=question)).first()
        
        return JsonResponse(model_to_dict(answer))
    else:
        return HttpResponse('Bad request..')

def checkout(request):
    if request.method == 'POST':
        cart = request.POST["cart"]
        address = request.POST["address"]
        governate = request.POST["governate"]
        payment = request.POST["payment"]
        user = request.user
        total = 0

        if cart:            
            cart = json.loads(cart)
    
            for item in cart:
                total = total + (float(item['price']) * item['qty'])

            order = Orders(user_id = user, address=address, governate=governate, payment_method = payment, total = total)
            order.save()
        
            for item in cart:
                product = Products.objects.filter(id=item['id']).get()
                order_item = Orders_items(order_id = order, product_id = product, price = item['price'], qty= item['qty'])
                order_item.save()
                
            return JsonResponse({"success": "true"})
                    
        return JsonResponse({"success": "false"})
    else:
        return HttpResponse('Bad request..')


def experts(request):
    videos = Videos.objects.all().order_by('-id')

    return render(request, 'experts.html', { 'videos': videos })


def thankyou(request):

    return render(request, 'thankyou.html')

def signup(request):
    if request.method == 'POST':
            username_unique_error = False
            email_unique_error = False
            # check if user does not exist
            if User.objects.filter(username=request.POST["username"]).exists():
                username_unique_error = True

            if User.objects.filter(email=request.POST["email"]).exists():
                email_unique_error = True

            if not email_unique_error and not username_unique_error:
                user = User.objects.create_user(username=request.POST["username"], password=request.POST["password"])
                user.first_name = request.POST["firstname"]
                user.last_name = request.POST["lastname"]
                user.email = request.POST["email"]
                user.is_active = True

                user.save()
                return redirect("/")
            else:
                return render(request, 'signup.html', {'signup_error': True})
            
    return render(request, 'signup.html')

def loginpage(request):
    if request.user.is_authenticated:
       return redirect("/")
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request=request, user=user)

            return redirect("home")
        else:
            return render(request, 'login.html', {'login_error': True})
        
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')

def profile(request):
    if request.user.is_authenticated == False:
       return redirect("login")
    
    if request.method == 'POST':
        user = User.objects.get(id=request.user.id)
        user.first_name = request.POST["firstname"]
        user.last_name = request.POST["lastname"]
        user.email = request.POST["email"]
        user.save()

        profile = Profile.objects.get(user=user)
        try:
            profile.address = request.POST["address"]
            profile.mobile = request.POST["mobile"]
            profile.save()
        except:
            profile = Profile(address = request.POST["address"], mobile = request.POST["mobile"], user = user)
            profile.save()

    return render(request, 'profile.html')

def watch(request, video_id):
    video = Videos.objects.filter(id=video_id).get()

    return render(request, 'watch.html', {'video': video})


def basket(request):
    if request.user.is_authenticated == False:
       return redirect("login")
    products = Products.objects.all().order_by('-id')

    return render(request, 'basket.html', { 'products': products })