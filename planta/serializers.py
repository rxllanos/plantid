from rest_framework import serializers
from .models import (Plant, Plant_data, HealthAssessment,DiseaseSuggestion, 
    Ingredient, NutrientDetail, Property, Flavonoid, CaloricBreakdown, 
    WeightPerServing, Recepy, IngredientRecepy
)

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__' 

class PlantDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant_data
        fields = '__all__' 

class HealthSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthAssessment
        fields = '__all__' 

class DeseaseSuggestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiseaseSuggestion
        fields = '__all__' 

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__' 

class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = NutrientDetail
        fields = '__all__' 

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__' 


class FlavonoidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flavonoid
        fields = '__all__' 


class CaloricBreakdownSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaloricBreakdown
        fields = '__all__' 


class WeightPerServingSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightPerServing
        fields = '__all__' 


class RecepySerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepy
        fields = '__all__' 


class IngredientRecepySerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredientRecepy
        fields = '__all__' 

class CombinedSerializer(serializers.ModelSerializer):
    Plant = PlantSerializer()
    Plant_data = PlantDataSerializer()
    HealthAssessment = HealthSerializer()
    DiseaseSuggestion = DeseaseSuggestionSerializer()
    Ingredient = IngredientSerializer()
    NutrientDetail = NutrientSerializer()
    Property = PropertySerializer()
    Flavonoid = FlavonoidSerializer()
    CaloricBreakdown = CaloricBreakdownSerializer()
    WeightPerServing = WeightPerServingSerializer()
    Recepy = RecepySerializer()
    IngredientRecepy = IngredientRecepySerializer()

    class Meta:
        model = Plant
        fields = '__all__'