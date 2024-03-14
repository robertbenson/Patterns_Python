# Using Classes for encapsulation compared to global variables

This is my quick reference for using alternatives to global variables. 
It is not by any means a guide as to which pattern is the best.

The choice between using classes and encapsulation versus global variables depends on the specific requirements and design principles of your code. 

In general, using classes and encapsulation is often considered a better practice than relying heavily on global variables. 

## Modularity and Organisation:
Classes allow you to encapsulate related data and behaviour into a single unit, promoting a modular and organised code structure.

With global variables, it can be challenging to maintain a clear structure, and it's easier for variables to be modified unexpectedly, leading to potential bugs.

## Code Reusability:
Classes promote code reusability since you can create instances of a class in different parts of your code, and each instance can maintain its state independently. 


Global variables can lead to code that is tightly coupled and less reusable, 
as any part of the code can modify them, making it harder to reason about the behavior of the program.

## Encapsulation:
Encapsulation, a fundamental principle of object-oriented programming (OOP), 
allows you to hide the implementation details of a class and expose only what is necessary. This helps in reducing dependencies between different parts of the code. 
Global variables lack encapsulation, making it harder to control access to and modification of data, which can lead to unintended side effects.

## Testing and Debugging:

Classes make it easier to test and debug code because you can isolate and test individual components (methods) of a class independently.
Global variables can make testing and debugging more challenging, as changes to global state can affect the behavior of different parts of the code.

## Namespace Pollution:

Overuse of global variables can lead to namespace pollution, 
where variable names clash and cause unintended consequences.
Classes provide a way to create isolated namespaces, 
reducing the risk of naming conflicts.


While classes and encapsulation are generally recommended, 
it's essential to consider the specific requirements of your project. 
In some cases, using global variables might be appropriate, but it's crucial to be mindful of the potential drawbacks mentioned above. Striking a balance and following good design principles will contribute to more maintainable and scalable code.

## Singleton Pattern


The singleton pattern is a software design pattern that restricts the instantiation of a class to a singular instance. 
One of the well-known "Gang of Four" design patterns. 
A singleton implementation may use lazy initialization in which the instance is created when the static method is first invoked.

## Monostate Pattern

The monostate pattern will create instances or objects with their own identity that all share the same internal state. 
It is often referred to as the Borg pattern in reference to The Borg in Star Trek. 
While being individuals in their own right, they all share the same collective consciousness or shared state.

## Other Useful Patterns

## Factory Pattern

The Factory Pattern is to define an interface for creating an object, but leave the choice of its type to the subclasses, 
deferring the instantiation to the subclasses. Objects are created by calling a factory method 
instead of calling a constructor.

## Builder Pattern

The Builder Pattern is a creational design pattern used to construct complex objects step by step. 
It separates the construction of a complex object from its representation. i.e. keep the process of putting 
it together separate from how it's actually represented or used in the program. This way, the same 
construction process can create different representations.
Imagine you have an order for a new laptop. You will pick the processor, ram, screen size, memory , mouse, warranty and many other options.
The builder pattern will allow for many different laptop variations.