from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator


def index(request):
    # getting the Products from database
    product_objects = Products.objects.all()

    # search part
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # pagination we want only certain amount of product showing
    paginator = Paginator(product_objects, 8)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)

    return render(request, 'shop/index.html', context={'products_objects': product_objects})


def detail(request, id):
    # getting the right product by id
    product_object = Products.objects.get(id=id)

    return render(request, 'shop/detail.html', context={'products_object': product_object})


def checkout(request):

    if request.method == "POST":
        items = request.POST.get('items', "")
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        address = request.POST.get('address', "")
        city = request.POST.get('city', "")
        state = request.POST.get('state', "")
        zipcode = request.POST.get('zipcode', "")
        total = request.POST.get('total', "")
        order = Order(items=items, name=name, email=email, address=address, city=city, state=state, zipcode=zipcode, total=total)
        order.save()

    return render(request, 'shop/checkout.html')
