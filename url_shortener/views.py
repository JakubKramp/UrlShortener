from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from url_shortener.models import Url
from url_shortener.serializers import ShortenUrlSerializer


class UrlViewSet(GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = Url.objects
    lookup_field = "short_url"
    serializer_class = ShortenUrlSerializer

    def create(self, request, *args, **kwargs):
        print('CREATING')
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        print("RETRIEVE")
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
