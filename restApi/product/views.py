from .models import Category
from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from rest_framework import generics

# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer