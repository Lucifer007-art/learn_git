class student:
    def __init__(self, name, age, city, marks):
        self.name = name
        self.age = age
        self.city = city
        self.marks = marks

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.city}")
        print(f"Marks: {self.marks}")

    def greetings(self):
        return f"Hello, my name is {self.name}, I am {self.age} years old, and I am from {self.city}, and I scored {self.marks} marks."

s1 = student("Alice", 20, "New York", 85)
s2 = student("Bob", 22, "Los Angeles", 90)

#s1.display()
#s2.display()
greet_message = s1.greetings()
#   print(greet_message)

object_list = []
object_list.append(s1)
object_list.append(s2)

for i in object_list:
    print(i.greetings())