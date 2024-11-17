from django.urls import path, include
from rest_framework import routers
from .views import MealViewSet, RatingViewSet, UserViewSet



router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('meals', MealViewSet)
router.register('rating', RatingViewSet)



urlpatterns = [
    path('', include(router.urls)),

]



