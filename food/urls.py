from django.urls import path, include
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('food/<int:pk>', views.food, name='detail'),
    path('create_item/', views.create_food, name='create'),
    path('update_item/<int:pk>', views.update_food, name='update'),
    path('delete_item/<int:pk>', views.delete_food, name='delete'),

]
