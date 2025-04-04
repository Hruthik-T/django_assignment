from django.shortcuts import render
from django.db.models import Q
from .models import Product, Category, Tag
from .forms import ProductFilterForm


def product_list(request):
    """
    View function for displaying products with search and filter functionality.
    """
    # Get all categories and tags for filter options
    categories = Category.objects.all()
    tags = Tag.objects.all()
    
    # Initialize queryset with all products
    products = Product.objects.all()
    
    # Initialize form
    form = ProductFilterForm(request.GET)
    
    # Process form if submitted
    if form.is_valid():
        # Search by description
        search_query = form.cleaned_data.get('search')
        if search_query:
            products = products.filter(
                Q(name__icontains=search_query) | 
                Q(description__icontains=search_query)
            )
        
        # Filter by category
        category_id = form.cleaned_data.get('category')
        if category_id:
            products = products.filter(category_id=category_id)
        
        # Filter by tags
        selected_tags = form.cleaned_data.get('tags')
        if selected_tags:
            # Django's ORM will handle the join for a many-to-many relationship
            products = products.filter(tags__in=selected_tags).distinct()
    
    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'form': form,
    }
    
    return render(request, 'products/product_list.html', context)
