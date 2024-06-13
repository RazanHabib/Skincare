from django.shortcuts import render, redirect
from store.models import Videos, Products, Orders, Orders_items, Profile, Chatbot, User, Categories, Recipes, Experts
from django.contrib.auth import logout, login, authenticate
from .forms import ExpertForm, ProductForm, RecipesForm, VideotForm

def home_view(request):
    if request.user.is_authenticated == False and request.user.is_staff == False:
       return redirect("/dashboard/signin")
    orders = Orders.objects.all().order_by('-id')[0:5]

    return render(request, 'index.html', { 'orders': orders })

def logout_view(request):
    logout(request)
    return redirect('/dashboard/signin')

def login_view(request):
    if request.user.is_authenticated and request.user.is_staff:
       return redirect("/dashboard/")
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None and user.is_staff:
            login(request=request, user=user)

            return redirect("index")
        else:
            return render(request, 'login_page.html', {'login_error': True})
        
    return render(request, 'login_page.html')

def categories_list(request):
    if request.method == "POST":
        item_id = request.POST['item_id']

        Categories.objects.filter(id=item_id).delete()

    categories = Categories.objects.all().order_by('-id')

    return render(request, 'categories_list.html', { 'categories': categories })

def new_category(request):
    if request.method == 'POST':
        category = Categories(title=request.POST['title'])
        category.save()

        return redirect("cats")
    
    return render(request, 'new_category.html')

def products_list(request, cat):
    if request.method == "POST":
        item_id = request.POST['item_id']

        Products.objects.filter(id=item_id).delete()

    category = Categories.objects.filter(id=cat).get()

    products = Products.objects.filter(category=category).order_by('-id')

    return render(request, 'products_list.html', { 'products': products, 'category': category })


def new_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('cats')

    return render(request, 'new_product.html', {'form': form})

def orders_list(request):

    if request.method == "POST":
        item_id = request.POST['item_id']

        Orders.objects.filter(id=item_id).delete()

    orders = Orders.objects.all()

    return render(request, 'orders_list.html', { 'orders': orders })

def order_details(request, order_id):

    user_prodile = None
    order_details = Orders.objects.filter(id=order_id).get()
    if order_details:
        user_prodile = Profile.objects.filter(user=order_details.user_id).get()
    order_items = Orders_items.objects.filter(order_id=order_details).all().order_by('-id')

    return render(request, 'order_details.html', { 'order_details': order_details, 'order_items': order_items, 'user_prodile': user_prodile })

def reports(request):

    total = 0
    if request.method == "POST":
        report_from = request.POST['from']
        report_to = request.POST['to']

        orders = Orders.objects.filter(date__range=[report_from,report_to]).all()
        for item in orders:
            total = float(total) + float(item.total)
    else:
        orders = None

    return render(request, 'reports.html', { 'orders': orders, 'total': total })

def recipes_list(request):

    if request.method == "POST":
        item_id = request.POST['item_id']

        Recipes.objects.filter(id=item_id).delete()

    recipes = Recipes.objects.all().order_by('-id')

    return render(request, 'recipes_list.html', { 'recipes': recipes })

def new_recipe(request):
    form = RecipesForm()
    if request.method == 'POST':
        form = RecipesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('recipes_list')

    return render(request, 'new_recipe.html', {'form': form})

def experts_list(request):

    if request.method == "POST":
        item_id = request.POST['item_id']

        Experts.objects.filter(id=item_id).delete()

    experts = Experts.objects.all().order_by('-id')

    return render(request, 'experts_list.html', { 'experts': experts })


def new_expert(request):
    form = ExpertForm()
    if request.method == 'POST':
        form = ExpertForm(request.POST, request.FILES, request.user)

        if form.is_valid():
            form.save()
            return redirect('experts_list')

    return render(request, 'new_expert.html', {'form': form})

def videos_list(request, expert_id):

    if request.method == "POST":
        item_id = request.POST['item_id']

        Videos.objects.filter(id=item_id).delete()

    expert = Experts.objects.filter(id=expert_id).get()
    videos = Videos.objects.filter(expert_id=expert).all().order_by('-id')

    return render(request, 'videos_list.html', { 'videos': videos, 'expert': expert, 'expert_id': expert_id })

def new_video(request, expert_id):
    form = VideotForm()
    if request.method == 'POST':
        form = VideotForm(request.POST, request.FILES, initial={"expert_id": expert_id})

        if form.is_valid():
            form.save()
            return redirect('experts_list')

    return render(request, 'new_video.html', {'form': form})

def chatbot_list(request):

    if request.method == "POST":
        item_id = request.POST['item_id']

        Chatbot.objects.filter(id=item_id).delete()

    chatbots = Chatbot.objects.all().order_by('-id')

    return render(request, 'chatbot_list.html', { 'chatbots': chatbots })


def new_chatbot(request):
    if request.method == 'POST':
        chatbots = Chatbot(question=request.POST['question'], answer=request.POST['answer'])
        chatbots.save()

        return redirect("chatbot_list")
    
    return render(request, 'new_chatbot.html')