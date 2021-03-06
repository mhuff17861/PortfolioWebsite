"""
    This file contains the tests which are used to verify that the resume app's models, views, templates, and
    their respective functions are all operating properly.
"""
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class ViewNoDataTests(TestCase):
    """Tests views in the portfolio_music_player app without feeding them model data"""

    def setup(self):
        self.client = Client()

    def test_player_no_data_response(self):
        """
            Test the index url for error free page return
        """
        response = self.client.get(reverse('music_player:player'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'portfolio_music_player/music_player.html')
