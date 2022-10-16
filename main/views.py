from django.shortcuts import render
from .models import Main, Home, About, Products, Contacts

# Create your views here.
def main(request):
    main = Main.objects.first()
    home = Home.objects.first()

    data = {'main': main,
            'home': home,
            }

    return render(request, 'main.html', context=data)


def about(request):
    about = About.objects.first()
    main = Main.objects.first()

    data = {'about': about,
            'main': main,
            }
    return render(request, 'about.html', context=data)


def pruducts(request):
    products = Products.objects.filter(is_visible=True)
    main = Main.objects.first()

    data = {'products': products,
            'main': main,
            }

    return render(request, 'products.html', context=data)


def contacts(request):
    contacts = Contacts.objects.first()
    main = Main.objects.first()

    data = {'contacts': contacts,
            'main': main,
            }

    return render(request, 'contacts.html', context=data)