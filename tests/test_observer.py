import unittest
from observer import ChannelPublisher
from observer import Subscriber


class Observer_TestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
        cls.channelPublisher = ChannelPublisher()
        cls.bob = Subscriber("Bob")
        cls.FooBar = Subscriber("FooBar")

    def test_register_2_observers(self):
        """ register 2 observers """
        self.channelPublisher.register(self.bob)
        self.assertEqual(len(self.channelPublisher.subscribers), 1)

        # register second observer
        self.channelPublisher.register(self.FooBar)
        self.assertEqual(len(self.channelPublisher.subscribers), 2)

    def test_sequence(self):
        """ notify,
        unregister ,
        unregister,
        notify"""
        self.channelPublisher.notify()
        self.channelPublisher.unregister(self.bob)
        self.assertEqual(len(self.channelPublisher.subscribers), 1)

        for subscriber in self.channelPublisher.subscribers:
            self.assertEqual(subscriber.name, "FooBar")
            self.assertEqual(subscriber.update(),
                             "new youtube video released FooBar")

        # verify that bob has actually been removed
        self.assertNotIn(self.bob, self.channelPublisher.subscribers)

        self.channelPublisher.unregister(self.FooBar)
        self.assertNotIn(self.FooBar, self.channelPublisher.subscribers)

        # verify that no more subscribers are left
        self.assertEqual(len(self.channelPublisher.subscribers), 0)
