from rest_framework import routers
from .views import ArtworkViewSet


router = routers.DefaultRouter()
router.register(r'artworks', ArtworkViewSet)

urlpatterns = router.urls