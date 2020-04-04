from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone
# Create your views here.
def home(request):
    products = product.objects
    return render(request, 'products/home.html', {'products':products})

@login_required(login_url = "/accounts/signup" )
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            prod = product()
            prod.title = request.POST['title']
            prod.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                prod.url = request.POST['url']
            else:
                prod.url ='http://' + request.POST['url']
                prod.icon = request.FILES['icon']
                prod.image = request.FILES['image']
                prod.pub_date = timezone.datetime.now()
                prod.hunter = request.user
                prod.save()
                return redirect('/products/' + str(prod.id))
        else:
            return render(request, 'products/create.html', {'error' : 'All fields are required'})
    else:
        return render(request, 'products/create.html')

def detail(request, prod_id):
    prod = get_object_or_404(product, pk=prod_id)
    return render(request, 'products/detail.html', {'prod':prod})

@login_required(login_url = "/accounts/signup" )
def upvote(request, prod_id):
    if request.method == 'POST':
        prod = get_object_or_404(product, pk=prod_id)
        prod.votes_total += 1
        prod.save()
        return redirect('/products/' + str(prod.id))
