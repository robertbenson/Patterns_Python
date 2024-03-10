import unittest
from observer import ChannelPublisher
from observer import Subscriber


class MyTestCase(unittest.TestCase):
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
        """ register , unregister, notify"""
        self.channelPublisher.notify()
        self.channelPublisher.unregister(self.bob)
        self.assertEqual(len(self.channelPublisher.subscribers), 1)
        subscribers = self.channelPublisher.subscribers

        for subscriber in self.channelPublisher.subscribers:
            self.assertEqual(subscriber.name, "FooBar")
            self.assertEqual(subscriber.update(),
                             "new youtube video released FooBar")

        # verify that bob has actually been removed
        self.assertNotIn(self.bob, self.channelPublisher.subscribers)

        self.channelPublisher.unregister(self.FooBar)
        self.assertNotIn(self.FooBar, self.channelPublisher.subscribers)

        # assert that no more subscibers are left
        self.assertEqual(len(self.channelPublisher.subscribers), 0)


