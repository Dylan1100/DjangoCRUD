from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductCreate
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# Create your views here.

def product_index(request):
    products = Product.objects.all()
    return render(request, 'products/product_index.html', {'products': products})

@login_required(login_url="/admin/login/")
def create_product(request):
    create = ProductCreate()
    if request.method == 'POST':
        create = ProductCreate(request.POST, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('product_index')
        else:
            return HttpResponse("""An error has occurred, <a href = "{{ url 'product_index'}}">click to reload</a>""")
    else:
        return render(request, 'products/product_create.html', {'product_create':create})

@login_required(login_url="/admin/login/")
def update_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('product_index')
    form = ProductCreate(request.POST or None, instance=product_sel)
    if form.is_valid():
       form.save()
       return redirect('product_index')
    return render(request, 'products/product_create.html', {'product_create':form})

@login_required(login_url="/admin/login/")
def delete_product(request, product_id):
    product_id = int(product_id)
    try:
        product_sel = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return redirect('product_index')
    product_sel.delete()
    return redirect('product_index')