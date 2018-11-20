from rest_framework import serializers

from .models import Recipe, MEAL_TYPES


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    meal = serializers.ChoiceField(choices=MEAL_TYPES, default='Lunch')
    instruction = serializers.CharField(
        allow_blank=True, required=False,
        style={'base_template': 'textarea.html'})
    wege = serializers.BooleanField(required=False)

    def create(self, validated_data):
        """
        Create and return a new Recipe instance, given the validated data.
        """
        return Recipe.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Recipe instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.title)
        instance.meal = validated_data.get('meal', instance.meal)
        instance.instruction = validated_data.get('instruction', instance.instruction)
        instance.wege = validated_data.get('wege', instance.wege)
        instance.save()
        return instance
