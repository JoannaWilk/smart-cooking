from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


urlpatterns = [
    path('recipes/', views.recipe_list),
    path('recipes/<int:pk>/', views.recipe_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
