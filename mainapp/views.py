from django.shortcuts import render

from mainapp.models import Product, Category


def index(reauest):
    context = {
        'products' : Product.objects.all()[:4]
    }
    return render(request, 'mainapp/index.html', context)




def products_list(request, pk=None):
    print(pk)
    links_menu = Category.objects.all()
    if pk is not None:
        if pk == 0:
            products_list = Product.objects.all()
            category_item = {'name': 'все', 'pk': 0}
        else:
            category_item = get_object_or_404(Category, pk=pk)
            products_list = Product.objects.filter(category_id=pk)

            context = {
                'links_menu': links_menu,
                'products': products_list,
                'category': category_item
            }

            return render(request, 'mainapp/products_list.html', context)

    context = {
        'links_menu': links_menu
    }
    return render(request, 'mainapp/products.html', context)


def contact(reaqest):
    return render(request, 'mainapp/contact.html')
