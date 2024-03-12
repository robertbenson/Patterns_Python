import unittest

from factory import PizzaFactory, MargheritaPizza, PepperoniPizza, Pizza


# Assume you have a PizzaFactory class and different Pizza subclasses (e.g.,
# MargheritaPizza, PepperoniPizza)

class TestPizzaFactory(unittest.TestCase):
    def test_create_margherita_pizza(self):
        pizza_factory = PizzaFactory()
        pizza = pizza_factory.create_pizza("Margherita")
        self.assertIsInstance(pizza, MargheritaPizza)
        # Add more specific assertions related to MargheritaPizza creation if needed

    def test_create_pepperoni_pizza(self):
        pizza_factory = PizzaFactory()
        pizza = pizza_factory.create_pizza("Pepperoni")
        self.assertIsInstance(pizza, PepperoniPizza)
        # Add more specific assertions related to PepperoniPizza creation if needed


    def test_abstract_class_instantiation(self):
        with self.assertRaises(Exception) as context:
            abstract_instance= Pizza()
            self.assertEqual(str(context.exception), "Concrete "
                                                     "implementation required")


if __name__ == '__main__':
    unittest.main()
