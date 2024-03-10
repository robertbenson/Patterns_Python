class Singleton:
    """A singleton class. Lazy instantiation, it is only created when needed"""
    __instance = None

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception(
                "Singleton already created, use get_instance() instead")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        """ this static method is associated with the class"""
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance


def main():
    singleton1 = Singleton.get_instance()
    singleton2 = Singleton.get_instance()
    singleton3 = Singleton.get_instance()

    print(singleton1)
    print(singleton2)
    print(singleton3)
    if singleton1 == singleton2 == singleton3:
        print("same memory location, pattern implemented correctly")

    singleton1.counter = 27    # one instance is updated
    print(singleton2.counter)  # change reflected in others


if __name__ == '__main__':
    main()
