from django.test import TestCase
from thestar.models import Competitor
from thestar.models import Vote
from factory import create_competitor

class TestVoteScreen(TestCase):
    def test_get_vote_screen(self):
        create_competitor()

        url = '/'
        response = self.client.get(url)
        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Kangsom')
        self.assertContains(response, 'Tanatat Chaiyaat')
        self.assertContains(response, '8')

    def test_vote(self):
        create_competitor()

        url = '/thestar/vote/?no=8'
        response = self.client.get(url)
        self.assertEqual(302, response.status_code)

        votes_for_ks = Vote.objects.all().count()
        self.assertEqual(1, votes_for_ks)