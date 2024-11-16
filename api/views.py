from rest_framework import viewsets, filters
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer






class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    lookup_field = 'slug'



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [filters.SearchFilter]
    # The search functionality in search_fields operates at the database level, unrelated to the serializer (2 RatingSerializer new fields).
    search_fields = ['meal__slug', 'user__username']


