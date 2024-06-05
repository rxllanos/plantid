from django.shortcuts import render
from planta.models import Plant_data


def index(request):
    plants = Plant_data.objects.all()
    context = {'plants':plants} 
    return render(request, "home.html", context=context)
