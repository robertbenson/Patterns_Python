# Product class
class Computer:
    def __init__(self, cpu, ram, storage, gpu, screen):
        self.CPU = cpu
        self.RAM = ram
        self.storage = storage
        self.GPU = gpu
        self.Screen = screen

    def __str__(self):
        return (((f"\nHigh End Computer : " + str(self.CPU) +
                  "," + str(self.RAM)) + ","
                 + str(self.storage)) + ","
                + str(self.Screen))


# Builder interface
class ComputerBuilder:
    def build_cpu(self):
        pass

    def build_ram(self):
        pass

    def build_storage(self):
        pass

    def build_gpu(self):
        pass

    def build_screen(self):
        pass

    def get_computer(self):
        pass


# Concrete builder
class HighEndComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer("Intel i9", "32GB", "1TB SSD",
                                 "NVIDIA Quadro",
                                 screen="17 Inch touch screen")

    def build_cpu(self):
        self.computer.CPU = "Intel i9"

    def build_ram(self):
        self.computer.RAM = "64GB"

    def build_storage(self):
        self.computer.storage = "2TB SSD"

    def build_gpu(self):
        self.computer.GPU = "NVIDIA Quadro"

    def build_screen(self):
        self.computer.Screen = "17 Inch touch screen"

    def get_computer(self):
        return self.computer

    def __str__(self):
        return (((f"\nHigh End Computer : " + str(self.computer.CPU) +
                  "," + str(self.computer.RAM)) + ","
                 + str(self.computer.storage)) + ","
                + str(self.computer.Screen))

class BudgetComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer("Intel i3", "8GB", "250MB HD",
                                 "NVIDIA",
                                 screen="13 Inch")

    def build_cpu(self):
        self.computer.CPU = "Intel i3"

    def build_ram(self):
        self.computer.RAM = "8GB"

    def build_storage(self):
        self.computer.storage = "250MB HD"

    def build_gpu(self):
        self.computer.GPU = "NVIDIA"

    def build_screen(self):
        self.computer.Screen = "13 Inch"

    def get_computer(self):
        return self.computer

    def __str__(self):
        return (((f"\nHigh End Computer : " + str(self.computer.CPU) +
                  "," + str(self.computer.RAM)) + ","
                 + str(self.computer.storage)) + ","
                + str(self.computer.Screen))


# Director
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_cpu()
        self.builder.build_ram()
        self.builder.build_storage()
        self.builder.build_gpu()
        self.builder.build_screen()


# Client code
builder = HighEndComputerBuilder()
director = ComputerDirector(builder)
director.construct_computer()
computer = builder.get_computer()


def print_spec(model: str, computer: Computer) -> None:
    print(f"\nComputer specs: {model}")
    print(f"CPU: {computer.CPU}")
    print(f"RAM: {computer.RAM}")
    print(f"Storage: {computer.storage}")
    print(f"GPU: {computer.GPU}")
    print(f"Screen: {computer.Screen}")


# Output for a High End model
print_spec("High End", computer)

# Client code
builder = BudgetComputerBuilder()
director = ComputerDirector(builder)
director.construct_computer()
computer = builder.get_computer()

# Output for a Budget model
print_spec("Budget", computer)

