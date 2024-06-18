from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('starter', 'Starter'),
    ('main_course', 'Main Course'),
    ('dessert', 'Dessert'),
]

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField()  
    serving_size = models.IntegerField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f'{self.recipe.title} - {self.rating}'
