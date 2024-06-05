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
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantrecepy = Recepy.objects.get(plant=plantingedient)
            ingedientrecepy = IngredientRecepy.objects.get(recepy=plantrecepy)
            serializer = IngredientRecepySerializer(ingedientrecepy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)
        
class RecepyAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantrecepy = Recepy.objects.get(plant=plantingedient)
            serializer = RecepySerializer(plantrecepy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)
        
class WeightPerServingAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantwps = WeightPerServing.objects.get(plant=plantingedient)
            serializer = WeightPerServingSerializer(plantwps)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class CaloricBreakdownAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantcbd = CaloricBreakdown.objects.get(plant=plantingedient)
            serializer = CaloricBreakdownSerializer(plantcbd)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class FlavonoidAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantflavonoid = Flavonoid.objects.get(plant=plantingedient)
            serializer = FlavonoidSerializer(plantflavonoid)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PropertyAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantnutrient = Property.objects.get(plant=plantingedient)
            serializer = PropertySerializer(plantnutrient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class NutrientAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            plantnutrient = NutrientDetail.objects.get(plant=plantingedient)
            serializer = NutrientSerializer(plantnutrient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PlantIngredientAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantData = Plant_data.objects.get(plant=plant)
            plantingedient = Ingredient.objects.get(plant=plantData)
            serializer = IngredientSerializer(plantingedient)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PlantDeseaseAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            plantHealth = HealthAssessment.objects.get(plant=plant)
            queryset = DiseaseSuggestion.objects.filter(health_assessment=plantHealth)
            serialized_data_list = []
            for q in queryset:
                serializer = DeseaseSuggestionSerializer(q)
                serialized_data_list.append(serializer.data)
            return Response(serialized_data_list, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PlantHealthAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            PlantHealth = HealthAssessment.objects.get(plant=plant)
            serializer = HealthSerializer(PlantHealth)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)

class PlantDataAPIView(APIView):
    def get(self, request, pk):
        try:
            plant = Plant.objects.get(access_token=pk)
            PlantData = Plant_data.objects.get(plant=plant)
            serializer = PlantDataSerializer(PlantData)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Plant_data.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)


def add(request):
    if request.method == "POST":
        form = PlantPictureForm(request.POST, request.FILES)
        if form.is_valid():
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
            plant = Plant.objects.get(access_token=pk)
            plant.delete()
            return render(request, "home")
        except Plant.DoesNotExist:
            return Response({'error': 'Plant not found'}, status=status.HTTP_404_NOT_FOUND)
