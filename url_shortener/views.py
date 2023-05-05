from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from url_shortener.models import Url
from url_shortener.serializers import ShortenUrlSerializer


class UrlViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Url.objects
    lookup_field = "short_url"
    serializer_class = ShortenUrlSerializer

