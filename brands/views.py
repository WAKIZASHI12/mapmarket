# brands/views.py
from django.shortcuts import render
from .models import Brand

def brand_location(request):
    if request.method == 'POST':
        brand_name = request.POST.get('brand_name')
        brands = Brand.objects.filter(name__icontains=brand_name)
    else:
        brands = Brand.objects.all()
    return render(request, 'brands/brand_location.html', {'brands': list(brands.values())})

def brand_search(request):
    return render(request, 'brands/brand_search.html')