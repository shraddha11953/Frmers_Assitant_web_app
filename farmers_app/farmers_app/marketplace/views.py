from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.seller = request.user
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'marketplace/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'marketplace/product_list.html', {'products': products})
