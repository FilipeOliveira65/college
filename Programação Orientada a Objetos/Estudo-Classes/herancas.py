class Mom:
    def __init__(self, color):
        self.color = color

class Child(Mom):
    def __init__(self, name, color):
        self.name = name
        super().__init__(color)

adult = Mom('Pink')
children = Child('Blue', 'Alice')

print(f'Mom: {vars(adult)} \nChild: {vars(children)}')



