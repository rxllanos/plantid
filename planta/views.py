from django.shortcuts import render, redirect
from .forms import PlantPictureForm
from django.contrib import messages
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import ( Plant, Plant_data, HealthAssessment,DiseaseSuggestion, 
    Ingredient, NutrientDetail, Property, Flavonoid, CaloricBreakdown, WeightPerServing, Recepy, IngredientRecepy
)

from .serializers import ( 
PlantSerializer, PlantDataSerializer, HealthSerializer, DeseaseSuggestionSerializer, IngredientSerializer, 
NutrientSerializer, PropertySerializer, FlavonoidSerializer, CaloricBreakdownSerializer,
WeightPerServingSerializer, RecepySerializer, IngredientRecepySerializer,
)

class RecepyIngredientAPIView(APIView):
    def get(self, request, pk):
        try:
            plantrecepy = Recepy.objects.get(recepy_id_recepy=pk)
            ingedientrecepy = IngredientRecepy.objects.filter(ingrecepy_recepy=plantrecepy)
            serialized_data_list = []
            for q in ingedientrecepy:
                serializer = IngredientRecepySerializer(q)
                serialized_data_list.append(serializer.data)
                return Response(serialized_data_list, status=status.HTTP_200_OK)   
        except Plant_data.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)
        
class RecepyAPIView(APIView):
    def get(self, request, pk):
        try:
            ing = Ingredient.objects.get(ingredient_id_Ingredient=pk)
            plantrecepy = Recepy.objects.filter(recepy_ingredient=ing)
            serialized_data_list = []
            for q in plantrecepy:
                serializer = RecepySerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)   
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)        
        
class WeightPerServingAPIView(APIView):
    def get(self, request, pk):
        try:
            ing = Ingredient.objects.get(ingredient_id_Ingredient=pk)
            plantwps = WeightPerServing.objects.get(wps_ingredient=ing)
            serializer = WeightPerServingSerializer(plantwps)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)    

class CaloricBreakdownAPIView(APIView):
    def get(self, request, pk):
        try:
            ing = Ingredient.objects.get(ingredient_id_Ingredient=pk)
            plantcbd = CaloricBreakdown.objects.get(cb_ingredient=ing)
            serializer = CaloricBreakdownSerializer(plantcbd)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)    

class FlavonoidAPIView(APIView):
    def get(self, request, pk):
        try:        
            ing = Ingredient.objects.get(ingredient_id_Ingredient=pk)
            plantf = Flavonoid.objects.filter(flavonoid_ingredient=ing)
            serialized_data_list = []
            for q in plantf:
                serializer = FlavonoidSerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)               
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)    

class PropertyAPIView(APIView):
    def get(self, request, pk):
        try:        
            ing = Ingredient.objects.get(ingredient_id_Ingredient=pk)
            plantproperty = Property.objects.filter(property_ingredient=ing)
            serialized_data_list = []
            for q in plantproperty:
                serializer = PropertySerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)    
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)    

class NutrientAPIView(APIView):
    def get(self, request, pk):
        try:
            ing = Ingredient.objects.get(ingredient_id_Ingredient=pk)
            plantnutrient = NutrientDetail.objects.filter(nutrient_ingredient=ing)
            serialized_data_list = []
            for q in plantnutrient:
                serializer = NutrientSerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)    

class PlantIngredientAPIView(APIView):
    def get(self, request, pk):
        try:
            plant_data = Plant_data.objects.get(plant_data_plant__plant_access_token=pk)
            queryset = Ingredient.objects.filter(ingredient_plant=plant_data)
            serialized_data_list = []
            for q in queryset:
                serializer = IngredientSerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)
        except Ingredient.DoesNotExist:
            return Response({'error': 'Ingredient not found'}, status=status.HTTP_404_NOT_FOUND)    

class PlantDeseaseAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(plant_access_token=pk)
            queryset = DiseaseSuggestion.objects.filter(disease_health_assessment__health_plant=plant)
            serialized_data_list = []
            for q in queryset:
                serializer = DeseaseSuggestionSerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PlantHealthAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(plant_access_token=pk)
            PlantHealth = HealthAssessment.objects.get(health_plant=plant)
            serializer = HealthSerializer(PlantHealth)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PlantDataAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(plant_access_token=pk)
            PlantData = Plant_data.objects.get(plant_data_plant=plant)
            serializer = PlantDataSerializer(PlantData)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)


def add(request):
    if request.method == "POST":
        form = PlantPictureForm(request.POST, request.FILES)
        if form.is_valid():
            plant_picture = form.save(commit=False)
            plant_picture.user = request.user
            form.save()
            messages.success(request, 'Data created Successfully!')
            return redirect('planta:add')
        else:
            messages.error(request, 'Error!')
            return render(request, 'planta/add.html', {'form': form})

    else:
        messages.success(request, 'Please fill out the form')
        return render(request, "planta/add.html", {
                "form": PlantPictureForm(),
        })

class PlantAPIView(APIView):
    def delete(self, request, pk):
        try:
            plant = Plant.objects.get(plant_access_token=pk)
            plant.delete()
            return render(request, "home")
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)
