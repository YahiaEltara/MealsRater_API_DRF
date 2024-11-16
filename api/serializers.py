from rest_framework import serializers
from .models import Meal, Rating





class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ('id', 'slug', 'title', 'description', 'no_of_rating', 'avg_rating')


class RatingSerializer(serializers.ModelSerializer):
    # meal = serializers.ReadOnlyField(source = 'meal.slug')
    # user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Rating
        fields = ('id', 'meal', 'user', 'stars')