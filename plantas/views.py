from django.shortcuts import render
from planta.models import Plant_data, Plant
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    user_plants = Plant.objects.filter(user=request.user)
    user_plant_data = Plant_data.objects.filter(plant_data_plant__in=user_plants)
    context = {'plants':user_plant_data} 
    return render(request, "home.html", context=context)
