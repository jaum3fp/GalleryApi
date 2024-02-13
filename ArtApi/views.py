from rest_framework import viewsets
from .models import Artwork
from .serializers import ArtworkSerializer
# Create your views here.



class ArtworkViewSet(viewsets.ModelViewSet):
    queryset = Artwork.objects.all()
    serializer_class = ArtworkSerializer