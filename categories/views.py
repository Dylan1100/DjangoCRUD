from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryCreate

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})

@login_required(login_url="/admin/login/")
def create_category(request):
    create = CategoryCreate()
    if request.method == 'POST':
        create = CategoryCreate(request.POST or None, request.FILES)
        if create.is_valid():
            create.save()
            return redirect('category_list')
        else:
            return HttpResponse("""That name already exists, <a href = "/categories/create/">click to reload</a>""")
    return render(request, 'categories/category_create.html', {'category_create':create})

@login_required(login_url="/admin/login/")
def update_category(request, category_id):
    category_id = int(category_id)
    try:
        category_sel = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('category_list')
    form = CategoryCreate(request.POST or None, instance=category_sel)
    if form.is_valid():
       form.save()
       return redirect('category_list')
    return render(request, 'categories/category_create.html', {'category_create':CategoryCreate})

@login_required(login_url="/admin/login/")
def delete_category(request, category_id):
    category_id = int(category_id)
    try:
        category_sel = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return redirect('category_list')
    category_sel.delete()
    return redirect('category_list')
