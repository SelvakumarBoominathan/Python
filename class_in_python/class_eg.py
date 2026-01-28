class Sample:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(f"Addtion is : {self.a + self.b}")

    def subtraction(self):
        print(f"subtraction is : {self.a - self.b}")

    def multiplication(self):
        print(f"multiplication is : {self.a * self.b}")

    def division(self):
        print(f"division is : {self.a / self.b}")


test = Sample(20, 29)

test.division()
