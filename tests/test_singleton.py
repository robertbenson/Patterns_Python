import unittest
from singleton import Singleton


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.s1 = Singleton.get_instance()
        cls.s2 = Singleton.get_instance()
        cls.s3 = Singleton.get_instance()

    def test_equal(self):
        """ same memory, instances will be same """

        self.assertEqual(self.s1, self.s2)
        self.assertEqual(self.s1, self.s3)

    def test_multiple_instances(self):
        """ all instances share the same internal state, should be equal """

        self.s1.some_variable = "I'm the only one"

        self.assertEqual(self.s1.some_variable, self.s2.some_variable)
        self.assertEqual(self.s1.some_variable, self.s3.some_variable)

    def test_incorrect_instantiation(self):
        """the singleton can only be created with get_instance, if a singleton
        is created using the __init__ an exception will be thrown.
        Test to verify the exception is thrown correctly."""

        with self.assertRaises(Exception) as context:
            s4 = Singleton()
        self.assertEqual(str(context.exception), "Singleton already created, "
                                                 "use get_instance() instead")


if __name__ == '__main__':
    unittest.main()
