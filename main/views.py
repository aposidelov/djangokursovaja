from django.shortcuts import redirect, render
from django.template.defaulttags import register
from .models import Restaurant, restaurant_field_labels
from .forms import RestaurantForm


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    restaurants = Restaurant.objects.all()
    types = dict(Restaurant.TYPE_CHOICES)
    return render(request, 'main/index.html',
                  context={'title': 'Ресторани та кафе у місті Дніпро', 'restaurants': restaurants, 'types': types, 'restaurant_field_labels': restaurant_field_labels})


def about(request):
    return render(request, 'main/about.html')


def entity_view(request, id=0):
    entity = Restaurant.objects.get(id=id)
    types = dict(Restaurant.TYPE_CHOICES)
    return render(request, 'main/entity_view.html', context={'entity': entity, 'types': types, 'restaurant_field_labels': restaurant_field_labels})


def entity_add(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RestaurantForm()
    context = {
        'title': 'Додати завід',
        'form': form,
        'restaurant_field_labels': restaurant_field_labels,
    }
    return render(request, 'main/entity_add.html', context=context)


def entity_update(request, id=0):
    entity = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=entity)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = RestaurantForm(instance=entity)
    context = {
        'title': 'Редагувати завід',
        'form': form,
        'restaurant_field_labels': restaurant_field_labels,
    }
    return render(request, 'main/entity_update.html', context=context)


def entity_delete(request, id=0):
    entity = Restaurant.objects.get(id=id)
    if request.method == 'POST':
        entity.delete()
        return redirect('home')
    form = RestaurantForm()
    context = {
        'title': 'Підтвердження на видалення заводу',
        'form': form,
        'entity_title': entity.title
    }
    return render(request, 'main/entity_delete.html', context=context)
