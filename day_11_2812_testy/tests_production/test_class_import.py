import unittest

from files_to_test.ubezpieczeni import Ubezpieczony
import datetime
from datetime import datetime
from dateutil import relativedelta


class TestUbezpieczeni(unittest.TestCase):
    def test_sample_value_1(self):
        person = Ubezpieczony("Adam 48", "1974-11-03", "Warszawa")
        self.assertEqual(person.old(), 49)

    def test_sample_value_2(self):
        person = Ubezpieczony("adam", "1970-11-03", "Warszawa")
        self.assertEqual(person.old(), 11)

    def test_sample_value_3(self):
        person = Ubezpieczony("Bad", "11-03-1974", "Warszawa")
        self.assertEqual(person.old(), 48)

#
# if __name__ == '__main__':
#     # to jest najprostsze
#     unittest.main()
