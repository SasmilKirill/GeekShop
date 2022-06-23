from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import revers
from adminapp.forms import UserAdminEditForm
from authapp.forms import ShopUserEditForm
from authapp.models import ShopUser


def user_create(request):
    return None


def user_read(request):
    context = {
        'objects': ShopUser.objects.all() .order_by('is_superuser')
    }
    return render(request,'adminapp / user_list.htmL', context)


def user_update(request, pk):
    user_item = get_object_or_404(ShopUser, pk=pk)
     if request.method == 'POST':
         edit_form = UserAdminEditForm(request.POST, request.FILES, instance=user_item)
         if edit_form.is_valid():
             edit_form.save()
             return HttpResponseRedirect(reverse('adminapp:user_update', args=[pk]))
     else:
         edit_form = UserAdminEditForm(instance=user_item)

    context = {
        'form': edit_form
    }
    return render(request, 'adminapp / user_form.html', context)

def user_delete(request, pk):
    user_item = get_object_or_484(ShopUser, pk=pk)
    if request.method == 'POST':
        user_item.is_active = False
        user_item.save()
        return HttpResponseRedirect(reverse('adminapp:user_read’))
    context = {
        'object': user_item
    }
    return render(request, 'adminapp / user_delete_confirm.htmL', context)

 def category_create(request):
     return None

def category_read(request):
    context = {

    }
    return render(request, 'adminapp / category_list.html', context)

def category_update(request):
    return None

def category_delete(request):
    return None

def products_read(request, pk):

    products_list = Products.objects.filter(category_id=pk)
    return None