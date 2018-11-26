from rest_framework import serializers

from .models import Recipe


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = Recipe
        fields = ('url', 'id', 'added_by',
                  'name', 'meal', 'instruction', 'wege')
