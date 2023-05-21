from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseNotFound
from MainApp.models import Item, Color
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
author_info = {
    'name': 'Vladimir',
    'surname': 'Voland',
    'email': '123@mail.ru'
}

# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]


def home(request):
    return render(request, 'index.html')


def about(request):
    context = {
        'author': author_info
    }

    return render(request, 'about.html', context)


def item_page(request, id):
    try:
        item = Item.objects.get(id=id)
        colors = item.colors.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id {id} не найден")
    context = {
        'item': item,
        'colors': colors,
    }
    return render(request, 'item-page.html', context)


def items_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }

    return render(request, 'items-list.html', context)


def item_add(request):
   if request.method == "GET":
       colors = Color.objects.all()
       context = {
           'colors' : colors
       }
       return render(request, "item-add.html", context)

# здесь получаем данные от формы заполнения/добавления в БД
def item_create(request):
   if request.method == "POST":
       form_data = request.POST
       colors_id = form_data.getlist('colors')
       item = Item(
           name=form_data['name'],
           brand=form_data['brand'],
           count=form_data['count'],
           description=form_data['description'],
       )
       item.save()
       for color in colors_id:
           item.colors.add(color)

       # print(f"{form_data=}")
       return redirect('items-list')
