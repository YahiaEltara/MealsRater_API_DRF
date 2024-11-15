from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator



# uuid

class Meal (models.Model):
    title = models.CharField(max_length=22)
    description = models.TextField(max_length=360)
    # slug = models.SlugField(blank=True, null=True)

    # def save (self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)      
    @property
    def slug(self):
        return slugify(self.title)

    def __str__(self):
        return self.title
    


class Rating (models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Rating for - {self.meal} - by {self.user}"
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields= ['meal', 'user'], name= 'unique_meal_user'),
        ]
        indexes = [
            models.Index(fields= ['meal', 'user']),
        ]



