from rest_framework.routers import SimpleRouter
from url_shortener.views import UrlViewSet

router = SimpleRouter()

router.register('', UrlViewSet)
