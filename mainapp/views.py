from django.shortcuts import render

def index(reauest):
    context = {
        'user_list' : [
        {
            'first_name': 'Oleg',
            'last_name': 'Maslow',
            'age': '31'
        },
            {
                'first_name': 'Eugeniy',
                'last_name': 'Demidov',
                'age': '33'
            }
        ]

    }
    return render(reauest, 'mainapp/index.html', context)

def products(reauest):
    return render(reauest, 'mainapp/products.html')

def contact(reauest):
    return render(reauest, 'mainapp/contact.html')
