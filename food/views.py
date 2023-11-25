from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import *

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from . forms import ItemForm
from django.urls import reverse


# Create your views here.


# def index(request):
#     items = Item.objects.all()
#     context = {
#         'items': items, 'title': 'Home'}
#     return render(request, 'index.html', context)


class IndexClassView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexClassView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        return context


# def food(request, pk):
#     food = Item.objects.get(id=pk)
#     context = {
#         'food': food, 'title': food}
#     return render(request, 'food.html', context)


class FoodDetailView(DetailView):
    model = Item
    template_name = 'food.html'
    # context_object_name = 'food'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(FoodDetailView, self).get_context_data(**kwargs)
        context['title'] = self.object.item_name
        context['author'] = 'Foliwe'
        return context


def create_food(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {'form': form, 'title': 'Add Food'}
    return render(request, 'add.html', context)


class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super(FoodCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Add Food'
        return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


@login_required()
def update_food(request, pk):
    food = Item.objects.get(id=pk)
    form = ItemForm(request.POST or None, instance=food)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    context = {'form': form, 'title': 'Update Food', 'food': food}
    return render(request, 'add.html', context)


@login_required()
def delete_food(request, pk):
    food = get_object_or_404(Item, id=pk)
    if request.method == 'POST':
        food.delete()
        return redirect('food:index')
    return render(request, 'delete.html', {'food': food})
