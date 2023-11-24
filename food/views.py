from django.shortcuts import get_object_or_404, render, redirect
from .models import *

from . forms import ItemForm


# Create your views here.


def index(request):
    items = Item.objects.all()
    context = {
        'items': items, 'title': 'Home'}
    return render(request, 'index.html', context)


def food(request, pk):
    food = Item.objects.get(id=pk)
    context = {
        'food': food, 'title': food}
    return render(request, 'food.html', context)


def create_food(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {'form': form, 'title': 'Add Food'}
    return render(request, 'add.html', context)


def update_food(request, pk):
    food = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {'form': form, 'title': 'Update Food', 'food': food}
    return render(request, 'add.html', context)


def delete_food(request, pk):
    food = get_object_or_404(Item, id=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food:index')
    return render(request, 'delete.html', {'food': food})
