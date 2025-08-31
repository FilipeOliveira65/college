class Mom:
    def __init__(self, color):
        self.color = color

class Child(Mom):
    def __init__(self, name):
        self.name = name

adult = Mom("Red")

children = Child("Blue")

print(adult.color)
print(children.color)
print(children.name)

