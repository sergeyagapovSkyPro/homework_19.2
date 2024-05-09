from django.shortcuts import render, get_object_or_404
from catalog.models import Product


def home(request):
    context = {'product_list': Product.objects.all()}
    return render(request, 'catalog/home.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'Ваше сообщение: {name}, {phone}, {message}')
        with open('write.txt', 'wt', encoding='UTF-8') as file:
            file.write(f'Ваше сообщение: {name}, {phone}, {message}')

    return render(request, 'catalog/contacts.html')


def product(request, pk):
    context = {'product': get_object_or_404(Product, pk=pk)}
    return render(request, 'catalog/product.html', context)
