from django.test import TestCase
from thestar.models import Competitor
from django.db import IntegrityError
from factory import create_competitor

class CompetitorTest(TestCase):
    def test_save_competitor(self):
        """
        The star should have these fields
        """
        kangsom = Competitor()
        kangsom.name = "Tanatat Chaiyaat"
        kangsom.nick_name = "Kangsom"
        kangsom.no = 8
        self.assertFalse(kangsom.id)
        kangsom.save()
        self.assertTrue(kangsom.id)

        kangsom_id = kangsom.id
        kangsom = Competitor.objects.get(id=kangsom_id)
        self.assertEqual('Tanatat Chaiyaat', kangsom.name)
        self.assertEqual('Kangsom', kangsom.nick_name)
        self.assertEqual(8, kangsom.no)

    def test_update_competitor(self):

        kangsom = Competitor.objects.create(name='Kangsom', nick_name='Kangsom', no=8)
        self.assertEqual('Kangsom', kangsom.nick_name)
        self.assertEqual('Kangsom', kangsom.name)
        self.assertEqual(8, kangsom.no)

        #update
        kangsom.name = 'Tanatat Chaiyaat'
        kangsom.save()

        new_kangsom = Competitor.objects.get(id=kangsom.id)
        self.assertEqual('Tanatat Chaiyaat', new_kangsom.name)
        self.assertEqual('Kangsom', new_kangsom.nick_name)
        self.assertEqual(8, new_kangsom.no)

    def test_no_must_be_unique(self):
        kangsom = Competitor.objects.create(name='Tanatat Chaiyaat', nick_name='Kangsom', no=8)

        hunz = Competitor()
        hunz.name = 'Isariya Phataramanop'
        hunz.nick_name = 'Hunz'
        hunz.no = 8
        self.assertRaises(IntegrityError, hunz.save)


