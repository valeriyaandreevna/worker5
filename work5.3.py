class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        if 0 < new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(floor)
        else:
            print("Такого этажа не существует")

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        return self.name == other.name and self.number_of_floors == other.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __add__(self, value):
        new_number = self.number_of_floors
        if isinstance(value, House):
            new_number += value.number_of_floors
        elif isinstance(value, int):
            new_number += value
        else:
            return NotImplemented
        return House(self.name, new_number)

    def  __iadd__(self, value):
        self.number_of_floors + value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors + value}'

    def  __radd__(self, value):
        self.number_of_floors + value
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors + value}'

    def __gt__(self, other):
        return self.name > other.name

    def __ge__(self, other):
        return self.name >= other.name

    def __it__(self, other):
        return self.name < other.name

    def __le__(self, other):
        return self.name <= other.name

    def __ne__(self, other):
        return self.name != other.name

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)
print(h1 == h2) #__eq__
h1 = h1 + 10 #__add__
print(h1)
print(h1==h2)
h1 += 10 # __iadd__
print(h1)
h2 = 10 + h2 # __radd__
print(h2)
print(h1 > h2) # __gt__ # false
print(h1 >= h2) # __ge__ #true!
print(h1 < h2) # __lt__ #false!
print(h1 <= h2) # __le__ #true
print(h1 != h2) # __ne__ #false

#объясните почему у меня тут не выдает не правильные значения...