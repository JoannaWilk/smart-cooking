from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeList(APIView):
    """List all recipes or create a new one."""

    def get(self, request, formay=None):
        recipes = Recipe.objects.all()
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecipeDetail(APIView):
    """Retrieve, update or delete a recipe."""

    def get_object(self, pk):
        try:
            return Recipe.objects.get(pk=pk)
        except Recipe.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def post(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
