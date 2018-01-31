from rest_framework import generics
from shortener.models import ShortURL
from .serializers import ShortURLSerializer

class DetailsShortURLView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShortURL.objects.all()
    serializer_class = ShortURLSerializer

class CreateShorturlView(generics.CreateAPIView):
    serializer_class = ShortURLSerializer
    