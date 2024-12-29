class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название: {self.name}, Количество этажей: {self.number_of_floors}')


    def go_to(self, new_floor):
        number_of_floors = self.number_of_floors

        list_gt = list(range(1, new_floor + 1))

        if int(new_floor) > number_of_floors or int(new_floor) < 1:
            print('Такого этажа не существует')
        else:
            for i in list_gt:
                print(i)


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

h1.__str__()
h2.__str__()

print(len(h1))
print(len(h2))