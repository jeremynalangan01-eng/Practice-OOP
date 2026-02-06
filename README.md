
class Human:
    the_num = []

    def __init__(self, name, age, height, salary):
        self.name = name
        self.age = age
        self.height = height
        self.salary = salary
        Human.the_num

    def walk(self):
        print(f"{self.name} is walking with the height of {self.height}")

    def talk(self):
        print(f"{self.name} is talking")

    def calculating(self):

        num = int(input(f"give number to {self.name}: "))
        self.the_num.append(num)

    def solving(self):
        op = input('+,-,/,*:')

        if op == "+":
            print(self.the_num[0] + self.the_num[1])

        if op == "-":
            print(self.the_num[0] - self.the_num[1])

        if op == "*":
            print(self.the_num[0] * self.the_num[1])

        if op == "/":
            print(self.the_num[0] / self.the_num[1])

human1 = Human("joe",67,"167cm","$57k")
human2 = Human("mike",8, "160cm","$12k")

print(human1.age)
print(human2.age)

human1.walk(),human2.walk(),human1.talk(),human2.talk()

human1.calculating()

human2.calculating()

human2.solving()

