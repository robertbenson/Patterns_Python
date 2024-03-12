import unittest
from monostate import Monostate


class Borg_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.borg1 = Monostate()
        cls.borg2 = Monostate()
        cls.borg3 = Monostate()

    def test_not_equal(self):
        """ different instances, memory will be different"""

        self.assertNotEqual(self.borg1, self.borg2)
        self.assertNotEqual(self.borg1, self.borg3)

    def test_multiple_instances(self):
        """all instances share the same internal state, should be equal"""

        self.borg1.some_variable = "Resistance is futile"

        self.assertEqual(self.borg1.some_variable, self.borg2.some_variable)
        self.assertEqual(self.borg1.some_variable, self.borg3.some_variable)

    def test_same_internal_state_dict(self):
        """all instances share the same internal state, should be equal
        verify __dict__ are the same for all instances"""

        self.borg1.counter = 27
        self.assertEqual(id(self.borg1.__dict__), id(self.borg2.__dict__))
        self.assertEqual(id(self.borg2.__dict__), id(self.borg3.__dict__))


if __name__ == '__main__':
    unittest.main()
