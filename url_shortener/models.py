import string
from secrets import choice

from django.db import models
from django.conf import settings


def get_short_url() -> str:
    """
    Simple function for generating short, random strings we use for url shortening.
    we use secrets.choice() because its less predictable than random.choice()
    :return: shortened url
    """
    allowed_chars = string.ascii_letters + string.digits
    return "".join([choice(allowed_chars) for _ in range(settings.URL_LENGTH)])


class Url(models.Model):
    """
    In the future consider removing urls created by anonymous users after certain amount of time
    """
    original_url = models.URLField(blank=False, null=False, unique=True)
    short_url = models.SlugField(default=get_short_url(), unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    #owner = models.ForeignKey('users.User', related_name='urls', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.original_url} shortened to {self.short_url}"
