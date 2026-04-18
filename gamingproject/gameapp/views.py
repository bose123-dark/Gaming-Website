from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Post, Order

def index(request):
    return render(request, "index.html")

def home(request):
    return render(request, "home.html")

def store(request):
    return render(request, "store.html")

def contact(request):
    return render(request, "contact.html")

def checkout(request):
    game_name = request.GET.get('game', "Marvel's Spider-Man 2")
    price = request.GET.get('price', "59.99")
    genre = request.GET.get('genre', "Action / Adventure")

    if request.method == 'POST':
        game = request.POST.get('game')
        edition = request.POST.get('edition', 'Standard')
        final_price = request.POST.get('final_price', '59.99')
        
        # Create the order
        order = Order.objects.create(
            user=request.user if request.user.is_authenticated else None,
            game_name=game,
            edition=edition,
            price=final_price
        )
        return render(request, "checkout.html", {
            'success': True, 
            'order_id': order.id,
            'game_name': game,
            'price': price,
            'genre': genre
        })

    return render(request, "checkout.html", {
        'game_name': game_name,
        'price': price,
        'genre': genre
    })

def blog(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, 'blog.html', {'posts': posts})

def library(request):
    orders = []
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-order_date')
    return render(request, "library.html", {'orders': orders})

def login_view(request):
    if request.method == 'POST':
        # Check if this is a registration or login request
        auth_type = request.POST.get('auth_type')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if auth_type == 'register':
            email = request.POST.get('email')
            if User.objects.filter(username=username).exists():
                return render(request, 'login.html', {'error': 'Neural ID already exists.'})
            
            # Create the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)
            return redirect('library')
        
        else: # Login
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('library')
            else:
                return render(request, 'login.html', {'error': 'Access Denied: Invalid Credentials.'})
                
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('index')


def article(request, slug):
    post = get_object_or_404(Post, slug=slug)
    # Fetch trending items (last 3 posts) for the sidebar
    trending = Post.objects.all().order_by('-date')[:3]
    return render(request, 'article.html', {'post': post, 'trending': trending})
