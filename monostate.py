class Monostate:
    """
    The Monostate or Borg pattern. This is another way to represent the
    Singleton pattern in Python. Instances will share the same state among
    instances,they do not occupy the same memory location. Changes to the
    shared state in one instance will be reflected in all instances. This
    allows instances to share data while maintaining their individuality.
    Usually, each instance will have its own dictionary, but the Borg
    pattern modifies this so that all instances have the same dictionary.
    While being individuals in their own right.  It is often referred to as
    the Borg pattern in reference to The Borg in Star Trek. They all share
    the same collective consciousness (in this case, _shared_state).
    """

    _shared_state = {'comment': 'Resistance is futile'}

    def __init__(self):
        self.__dict__ = self._shared_state


def process_monostate():
    """ This method will create 3 monostate objects.
    """
    borg1 = Monostate()
    borg2 = Monostate()
    borg3 = Monostate()

    # these are different objects, different memory locations

    print(f"different, expected for Monostate objects correctly: ")
    print('Borg1 object:{}'.format(borg1))
    print('Borg2 object:{}'.format(borg2))
    print('Borg3 object:{}'.format(borg3))

    borg1.counter = 27

    # counter has been set to 27 for only 1 borg object, however all
    # instances have the value 27 as they all share the same internal state.

    print('Borg1 state:{}'.format(borg1.__dict__))
    print('Borg2 state:{}'.format(borg2.__dict__))
    print('Borg3 state:{}'.format(borg2.__dict__))


def main():
    process_monostate()


if __name__ == '__main__':
    main()
