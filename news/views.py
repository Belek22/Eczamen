from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator
from news.models import Product
from django.db.models import Q

def main(request):
    products = Product.objects.all()  

    paginator = Paginator(products, 8)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'news': page_obj})

def news_list(request):
    query = request.GET.get('search') 
    products = Product.objects.all()

    if query:
        products = products.filter(
            Q(title__icontains=query) | 
            Q(category__name__icontains=query) 
        )

    paginator = Paginator(products, 8)  

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'news': page_obj})

def detail_news(request, pk):
    news = get_object_or_404(Product, pk=pk)
    return render(request, 'detail_news.html', {'news': news})
