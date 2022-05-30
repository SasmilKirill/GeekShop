from django.shortcuts import render

def index(reauest):
    return render(reauest, 'mainapp/index.html')

def products(reauest):
    return render(reauest, 'mainapp/products.html')

def contact(reauest):
    return render(reauest, 'mainapp/contact.html')
