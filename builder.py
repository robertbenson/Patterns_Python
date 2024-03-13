# Product class
class Computer:
    def __init__(self, CPU, RAM, storage, GPU):
        self.CPU = CPU
        self.RAM = RAM
        self.storage = storage
        self.GPU = GPU


# Builder interface
class ComputerBuilder:
    def build_CPU(self):
        pass

    def build_RAM(self):
        pass

    def build_storage(self):
        pass

    def build_GPU(self):
        pass

    def get_computer(self):
        pass


# Concrete builder
class HighEndComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer("Intel i9", "32GB", "1TB SSD",
                                 "NVIDIA RTX 3090")

    def build_CPU(self):
        self.computer.CPU = "Intel i9"

    def build_RAM(self):
        self.computer.RAM = "64GB"

    def build_storage(self):
        self.computer.storage = "2TB SSD"

    def build_GPU(self):
        self.computer.GPU = "NVIDIA RTX 3090"

    def get_computer(self):
        return self.computer


# Director
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct_computer(self):
        self.builder.build_CPU()
        self.builder.build_RAM()
        self.builder.build_storage()
        self.builder.build_GPU()


# Client code
builder = HighEndComputerBuilder()
director = ComputerDirector(builder)
director.construct_computer()
computer = builder.get_computer()

# Output
print("Computer specs:")
print(f"CPU: {computer.CPU}")
print(f"RAM: {computer.RAM}")
print(f"Storage: {computer.storage}")
print(f"GPU: {computer.GPU}")
