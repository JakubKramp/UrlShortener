from rest_framework import serializers

from url_shortener.models import Url


class ShortenUrlSerializer(serializers.ModelSerializer):

    class Meta:
        model = Url
        fields = ["original_url", "short_url"]