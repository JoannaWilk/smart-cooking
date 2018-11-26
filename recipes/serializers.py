from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = Recipe
        fields = ('id', 'name', 'meal', 'instruction', 'wege', 'added_by')
