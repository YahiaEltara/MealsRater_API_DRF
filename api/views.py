from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Meal, Rating
from .serializers import MealSerializer, RatingSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated





class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    # lookup_field = 'slug'


    @action(methods= ['POST'], detail= True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            meal = get_object_or_404(Meal, id=pk)
            username = request.data['username']
            user = get_object_or_404(User, username=username)
            stars = request.data['stars']

            try:
                # update
                rating = Rating.objects.get(meal = meal.id, user=user.id)
                rating.stars = stars
                rating.save()
                serializer_data = RatingSerializer (rating, many = False).data
                json = {'message': 'Rating updated successfully',
                        'result' : serializer_data
                        }
                return Response(json, status=status.HTTP_200_OK)

            except:
                # create if the rate is not exist
                rating = Rating.objects.create(user= user, meal= meal, stars= stars)
                serializer_data = RatingSerializer(rating, many = False).data
                json = {'message': 'Rating created successfully',
                        'result' : serializer_data
                        }
                return Response(json, status=status.HTTP_201_CREATED)


        else:
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = [filters.SearchFilter]
    # The search functionality in search_fields operates at the database level, unrelated to the serializer (2 RatingSerializer new fields).
    search_fields = ['meal__slug', 'user__username']

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def update (self, request, *args, **kwargs):
        json = {
            'message': 'It can not be used to update .. (:'
        }
        return Response(json, status=status.HTTP_400_BAD_REQUEST)
    
    def create (self, request, *args, **kwargs):
        json = {
            'message': 'It can not be used to create .. (:'
        }
        return Response(json, status=status.HTTP_400_BAD_REQUEST)


