class Employer:
    def __init__ (self, name, position):
        self.name = name
        self.position = position

employer1 = Employer("Filipe", "Software Developer")
employer2 = Employer("Ana Caroline", "Nurse")

print(f"Hello, {employer1.name}. Your position is {employer1.position}")

