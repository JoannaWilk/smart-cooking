from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    recipes = serializers.HyperlinkedRelatedField(
        many=True, view_name='recipe-detail', read_only=True
    )

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'recipes')
