
class Animal(object):
    """
    Aimal class
    """

    def __init__(self, color, name, type_='Cat'):
        self.type = type_
        self.color = color
        self.name = name

    def print_type(self):
        print('The type of animal is {}'.format(self.type))

    def print_name(self):
        print('The name of animal is {}'.format(self.name))


a1 = Animal('Black', 'John')
print(a1)
print(a1.print_name())
print(a1.print_type())

a1 = Animal('Black', 'John', 'Dog')
print(a1)
print(a1.print_name())
print(a1.print_type())


class Subclass(Animal):
    animal = Animal.color

