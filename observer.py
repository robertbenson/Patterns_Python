class Observer:
    """Observer interface"""

    def __init__(self):
        self.name = None

    def update(self):
        print("Subclass must implement update()")


class Subscriber(Observer):
    """ Subscriber class implemented the Observer interface"""

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name

    def update(self):
        s = F"new youtube video released {self.name}"
        print(s)
        return s

class Publisher:
    def register(self, subscriber: Subscriber) -> None:
        raise NotImplemented("Subclass must implement register()")

    def unregister(self, subscriber: Subscriber) -> None:
        raise NotImplemented("Subclass must implement unregister()")

    def notify(self) -> None:
        raise NotImplemented("Subclass must implement notify()")


class ChannelPublisher(Publisher):
    def __init__(self) -> None:
        super().__init__()
        self.subscribers = []  # observers

    def register(self, subscriber: Subscriber) -> None:
        self.subscribers.append(subscriber)

    def unregister(self, subscriber: Subscriber) -> None:
        self.subscribers.remove(subscriber)

    def notify(self) -> None:
        for subscriber in self.subscribers:
            subscriber.update()


def main():
    bob = Subscriber("Bob")
    cody = Subscriber("Cody")
    channelPublisher = ChannelPublisher()

    channelPublisher.register(bob)
    channelPublisher.register(cody)
    channelPublisher.notify()   # new youtube released, notify all
    # subscribers/observers
    channelPublisher.unregister(cody)
    channelPublisher.notify()
    channelPublisher.unregister(bob)
    channelPublisher.notify()


if __name__ == '__main__':
    main()
