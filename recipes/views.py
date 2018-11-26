from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from recipes.models import Recipe
from recipes.permissions import IsOwnerOrReadOnly
from recipes.serializers import RecipeSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'recipes': reverse('recipe-list', request=request, format=format)
    })


class RecipeList(generics.ListCreateAPIView):
    """List all recipes or create a new one."""

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(added_by=self.request.user)


class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    """Retrieve, update or delete a recipe."""

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
