"""
Tests for Django
"""
import datetime
from django.utils import unittest, timezone
from bibliographies.models import Bibliography


class BibliographyTestCase(unittest.TestCase):

    def setUp(self):
        self.bibwithoutspace = Bibliography(name="Friction")
        self.bibwithspace = Bibliography(
            name="The Effects of the coeficent of friction on stopping distance.",
            create_date=timezone.now())

    def test_bibliography_without_space_represented_correctly(self):
        """
        Asserts that bibliographies with spaces are represtented correctly
        """
        self.assertEqual(self.bibwithoutspace.__unicode__(), u'Friction')

    def test_bibliography_with_space_represented_correctly(self):
        """
        Asserts that bibliographies with spaces are represtented correctly
        """
        self.assertEqual(self.bibwithspace.__unicode__(),
                         u'The Effects of the coeficent of friction on stopping distance.')

    def test_future_bibliography_wasnt_created_recently(self):
        future_bib = Bibliography(name='test',
                                  create_date=timezone.now()
                                  + datetime.timedelta(days=30))
        self.assertEqual(future_bib.was_created_recently(), False)
