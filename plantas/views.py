from django.shortcuts import render
from planta.models import Plant_data, Plant, Ingredient,NutrientDetail,Property,Flavonoid, CaloricBreakdown
from django.contrib.auth.decorators import login_required
import ast

@login_required
def index(request):
    user_plants = Plant.objects.filter(user=request.user)
    user_plant_data = Plant_data.objects.filter(plant_data_plant__in=user_plants)
    plant_data_with_details = []
    for plant_data in user_plant_data:
        ingredients = Ingredient.objects.filter(ingredient_plant=plant_data)
        ingredient_details = []
        for ingredient in ingredients:
            nutrient_details = NutrientDetail.objects.filter(nutrient_ingredient=ingredient)
            property_details = Property.objects.filter(property_ingredient=ingredient)
            flavonoid_details = Flavonoid.objects.filter(flavonoid_ingredient=ingredient)
            caloric_breakdown = CaloricBreakdown.objects.filter(cb_ingredient=ingredient).first()
            
            ingredient_details.append({
                'ingredient': ingredient,
                'nutrients': nutrient_details,
                'properties': property_details,
                'flavonoids': flavonoid_details,
                'caloric_breakdown': caloric_breakdown
            })
        common_names_list = ast.literal_eval(plant_data.plant_data_common_names)
        plant_data_with_details.append({
            'plant_data': plant_data,
            'ingredient_details': ingredient_details,
            'common_names_list': common_names_list
        })
    context = {'plants_with_details':plant_data_with_details} 
    return render(request, "home.html", context=context)
