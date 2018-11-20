from django.db import models

MEAL_TYPES = (
    ('B', 'Breakfast'),
    ('D', 'Dinner'),
    ('L', 'Lunch'),
    ('S', 'Snack'),
    ('DS', 'Dessert'),
)


class Recipe(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=300)
    meal = models.CharField(choices=MEAL_TYPES, default='L', max_length=20)
    instruction = models.TextField(blank=True)
    wege = models.BooleanField(blank=True, default=True)

    class Meta:
        ordering = ('created',)
