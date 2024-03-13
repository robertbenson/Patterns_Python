# Define a Pizza interface
from abc import abstractmethod


class Pizza:
    @abstractmethod
    def prepare(self):
        return "Concrete implementation required"


    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass

# Concrete Pizza classes
class MargheritaPizza(Pizza):

    def prepare(self):
        print("Preparing Margherita Pizza")

    def bake(self):
        print("Baking Margherita Pizza")

    def cut(self):
        print("Cutting Margherita Pizza")

    def box(self):
        print("Boxing Margherita Pizza")

class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing Pepperoni Pizza")

    def bake(self):
        print("Baking Pepperoni Pizza")

    def cut(self):
        print("Cutting Pepperoni Pizza")

    def box(self):
        print("Boxing Pepperoni Pizza")

# Pizza Factory
class PizzaFactory:
    """It creates and returns an instance of the appropriate subclass based
    on the pizza_type parameter."""
    def create_pizza(self, pizza_type):
        if pizza_type == 'Margherita':
            return MargheritaPizza()
        elif pizza_type == 'Pepperoni':
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type")

# Client code
if __name__ == "__main__":
    # Creating a Margherita Pizza using the factory
    factory = PizzaFactory()
    pizza = factory.create_pizza('Margherita')

    # Using the created Margherita Pizza
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()

    # Creating a Pepperoni Pizza using the factory
    pizza = factory.create_pizza('Pepperoni')

    # Using the created Pepperoni Pizza
    pizza.prepare()
    pizza.bake()
    pizza.cut()
    pizza.box()
