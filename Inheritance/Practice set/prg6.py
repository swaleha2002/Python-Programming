# # Write __str__() method to print the vector as follows:
#  7i + 8j +10k
# Assume vector of dimension 3 for this problem

class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    # Corrected the method name to __add__
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result

    # Corrected the method name to __mul__
    def __mul__(self, other):
        # The dot product is a scalar value, not a vector, so this should return a single value.
        result = self.x * other.x + self.y * other.y + self.z * other.z
        return result

    # Corrected the method name to __str__
    def __str__(self):
        return f"({self.x}i+ {self.y}j+{self.z}k)"

# Example usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)

# v1 + v2 is a vector, so it makes sense to print it
print(v1 + v2)

# v1 * v2 is a scalar (dot product), so this will print a number
print(v1 * v2)
