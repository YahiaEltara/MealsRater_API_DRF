from rest_framework import serializers
from .models import Meal, Rating





class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('slug', 'title', 'description')


class RatingSerializer(serializers.ModelSerializer):
    meal = serializers.ReadOnlyField(source = 'meal.slug')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rating
        fields = ('meal', 'user', 'stars')