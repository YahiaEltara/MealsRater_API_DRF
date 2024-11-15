from django.urls import path, include
from rest_framework import routers
from .views import MealViewSet, RatingViewSet



router = routers.DefaultRouter()
router.register('meals', MealViewSet)
router.register('rating', RatingViewSet)



urlpatterns = [
    path('', include(router.urls)),

]



