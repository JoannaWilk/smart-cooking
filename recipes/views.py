from rest_framework import generics

from recipes.models import Recipe
from recipes.serializers import RecipeSerializer


class RecipeList(generics.ListCreateAPIView):
    """List all recipes or create a new one."""

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a recipe."""

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
