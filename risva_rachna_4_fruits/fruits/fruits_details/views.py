from rest_framework import generics
from .models import Fruit
from .serializer import FruitSerializer
from django.shortcuts import render, redirect
from .forms import FruitForm

def index(request):
    return render(request, 'index.html')

class FruitList(generics.ListAPIView):
    queryset = Fruit.objects.all().order_by('color')
    serializer_class = FruitSerializer
    template_name = 'fruits_list.html'

def fruit_add(request):
    if request.method == 'POST':
        form = FruitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fruit-list')
    else:
        form = FruitForm()
    return render(request, 'fruits_add.html', {'form': form})
