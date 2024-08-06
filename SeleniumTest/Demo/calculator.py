print("Operators:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")


class Calculator:
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def add(self):
        return n1 + n2

    def subtract(self):
        return n1 - n2

    def multi(self):
        return n1 * n2

    def division(self):
        return n1 / n2


while True:
    choice = input("Enter your choice: ")

    if choice in ('1', '2', '3', '4'):
        try:
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number: "))
            cal = Calculator(n1, n2)
        except ValueError:
            print("Invalid number")

        if choice == '1':
            print(n1, "+", n2, "=", cal.add())

        elif choice == '2':
            print(n1, "-", n2, "=", cal.subtract())

        elif choice == '3':
            print(n1, "*", n2, "=", cal.multi())

        elif choice == '4':
            print(n1, "/", n2, "=", cal.division())
            break
    else:
        print("Invalid")