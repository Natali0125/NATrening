class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    # 1. __eq__ - перегрузка
    def __eq__(self, other):
        if isinstance(other, (int, House)):         # не получается вывести сообщение об
            return self.number_of_floors == other.number_of_floors  # разных типах данных

    # 2. __lt__(self, other):
    def __lt__(self, other):
        if isinstance(other, (int,House)):
            return self.number_of_floors < other.number_of_floors


    def __le__(self, other):
        if isinstance(other, (int,House)):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, (int,House)):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, (int,House)):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, (int, House)):
            return self.number_of_floors != other.number_of_floors

    # 3 __add__(self, value)
    def __add__(self, value):
        number_of_floors = self.number_of_floors
        if isinstance(value, (int, House)):
            number_of_floors = number_of_floors + value
            self.number_of_floors = number_of_floors
        return self

    # 4  __radd__(self, value), __iadd__(self, value)
    def __iadd__(self, other):
        number_of_floors = self.number_of_floors
        if isinstance(other, (int, House)):
            number_of_floors +=  other
            self.number_of_floors = number_of_floors
        return self

    def __radd__(self, value):
        self.number_of_floors = value + self.number_of_floors
        return self


    def go_to(self, new_floor):

        number_of_floors = self.number_of_floors
        # print('number_of_floors', id(number_of_floors), 'self.number_of_floors', id(self.number_of_floors))
        list_gt = list(range(1, new_floor + 1))
        if int(new_floor) > number_of_floors or int(new_floor) < 1:
            print('Такого этажа не существует')
        else:
            for i in list_gt:
                print(i)


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)
print(h2)
print(h1 == h2)

h1 = h1 + 10  #  __add__
print(h1)
print(h1 == h2)  # __eq__

h1 += 10  #  __iadd__
print(h1)

h2 = 10 + h2  #  __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  #  __ge__
print(h1 < h2)  #  __lt__
print(h1 <= h2)  #  __le__
print(h1 != h2)  #  __ne__


