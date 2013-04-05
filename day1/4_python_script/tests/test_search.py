import search
from unittest import TestCase

echo_log = []

def mocked_echo(message):
    echo_log.append(message)

class TestSearch(TestCase):
    def setUp(self):
        self.original_echo = search.echo
        search.echo = mocked_echo

    def tearDown(self):
        search.echo = self.original_echo

    def assertEcho(self, message):
        print echo_log
        self.assertEqual(message, echo_log.pop())

    def test_search(self):
    	command = './search'
        status_code = search.main()
        self.assertEcho('A python is a constricting snake belonging to the Python (genus) , or, more generally, any snake in the family Pythonidae (containing the Python genus).')