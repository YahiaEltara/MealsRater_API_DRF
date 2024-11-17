from rest_framework import serializers
from .models import Meal, Rating
from django.contrib.auth.models import User





class UserSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}




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