import unittest

from builder import HighEndComputerBuilder


class TestBuilder(unittest.TestCase):
    def test_create_HighEndComputer(self):
        builder = HighEndComputerBuilder()
        computer = builder.get_computer()
        self.assertEqual(str(builder),
                         "\nHigh End Computer : Intel i9,32GB,1TB SSD,17 Inch touch screen")
        self.assertEqual(str(computer.CPU), "Intel i9")
        self.assertEqual(str(computer.RAM), "32GB")
        self.assertEqual(str(computer.storage), "1TB SSD")
        self.assertEqual(str(computer.GPU), "NVIDIA Quadro")
        self.assertEqual(str(computer.Screen), "17 Inch touch screen")


if __name__ == '__main__':
    unittest.main()
