from rest_framework import generics
from .models import FoodCategory
from .serializers import FoodListSerializer
from django.db import models

class FoodListView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        return FoodCategory.objects.prefetch_related('food').annotate(
            has_published_foods=models.Count('food', filter=models.Q(food__is_publish=True))).filter(has_published_foods__gt=0)

