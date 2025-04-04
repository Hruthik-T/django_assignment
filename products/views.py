from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, Tag
from .forms import ProductFilterForm


def product_list(request):
    """
    View function for displaying products with search and filter functionality.
    """
    categories = Category.objects.all()
    tags = Tag.objects.all()
    products = Product.objects.all()
    
    form = ProductFilterForm(request.GET)
    if form.is_valid():
        search_query = form.cleaned_data.get('search')
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        category_id = form.cleaned_data.get('category')
        if category_id:
            products = products.filter(category_id=category_id)
        
        selected_tags = form.cleaned_data.get('tags')
        if selected_tags:
            products = products.filter(tags__in=selected_tags).distinct()
    
    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'form': form,
    }
    
    return render(request, 'products/product_list.html', context)
