class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        number_of_floors = self.number_of_floors

        list_gt = list(range(1, new_floor + 1))

        if int(new_floor) > number_of_floors or int(new_floor) < 1:
            print('Такого этажа не существует')
        else:
            for i in list_gt:
                print(i)
h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h3 = House('ЖК Эльбрус', 30)

h1.go_to(5)

h2.go_to(10)

#h3.go_to(25)


