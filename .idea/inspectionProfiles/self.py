class Computer:
    def __init__(self):
        self.name = "Aman"
        self.age = 43

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

# Create objects outside the class
c1 = Computer()
c1.age = 45
c2 = Computer()

# Compare the objects
if c1.compare(c2):
    print("They are the same")
else:
    print("They are different")

# Print the names of the objects
print(c1.name)
print(c2.name)
