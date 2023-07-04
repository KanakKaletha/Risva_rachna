from django.urls import path
from .views import index, FruitList, fruit_add

urlpatterns = [
    # path('', index, name='index'),
    path('fruits/', FruitList.as_view(), name='fruit-list'),
    path('fruits/add/', fruit_add, name='fruit-add'),
]

