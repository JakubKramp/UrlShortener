from django.test import TestCase
from django.urls import reverse

from url_shortener.models import Url


class UrlShortenerTestCase(TestCase):

    def test_shorten_url(self):
        url = "https://pl.wikipedia.org/wiki/Real_Madryt"
        self.client.post('', data={'original_url': url})

        self.assertEqual(1, Url.objects.count())
        url_obj = Url.objects.get(original_url=url)
        response = self.client.get(reverse('url-detail', kwargs={"short_url": url_obj.short_url}))
        self.assertEqual(response.data['short_url'], url_obj.short_url)
        self.assertEqual(response.data['original_url'], url)

    def test_create_existing_url(self):
        url = "https://pl.wikipedia.org/wiki/Real_Madryt"
        Url.objects.create(original_url=url)
        self.client.post('', data={'original_url': url})

        self.assertEqual(1, Url.objects.count())
        url_obj = Url.objects.get(original_url=url)
        response = self.client.get(reverse('url-detail', kwargs={"short_url": url_obj.short_url}))
        self.assertEqual(response.data['short_url'], url_obj.short_url)

    def test_create_specific_url(self):
        url = "https://pl.wikipedia.org/wiki/Real_Madryt"
        short_url = 'short'
        self.client.post('', data={'original_url': url, 'short_url': short_url})

        self.assertEqual(1, Url.objects.count())
        response = self.client.get(reverse('url-detail', kwargs={"short_url": short_url}))
        self.assertEqual(response.data['short_url'], short_url)
