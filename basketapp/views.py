


def basket_list(requests):
    context = {
        'baskets': Basket.objects.filter(user=request.user)
    }

    return render(request, 'basketapp/list', context)





def basket_add(reauest, pk):
    product_item = get_object_or_404(Product, pk=pk)

    basket_item = Basket.objects.filter(product=product_item, user=request.user).fiers()

    if not basket_item:
        basket_item = Basket(product=product_item, user=request.user)


    basket_item.quantity += 1
    basket_item.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))






def basket_remove(request, pk):
    Basket.objects.filter(pk=pk).delete()
    return HttpResponseRedirect('')
