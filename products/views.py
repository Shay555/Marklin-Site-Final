from django.shortcuts import render
from .models import Product
from forms import ProductForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def all_products(request):
    products = Product.objects.all()

    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    return render(request, "products.html", {"products": products})




def new_listing (request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(all_products)
    else:
        form = ProductForm()
    return render(request, 'Sell-Item.html', {
        'form': form
    })



