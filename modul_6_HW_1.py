#Наследование классов


#
# ###
# # Первый вариант:
#
class Animal: #Родительский класс
    alive = True # живой - да
    fed = False  # накормленный - нет
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        #food = Plant(self.name)
        if food.edible == True:
            print('food.edible=', food.edible, ' - съедобный')  # # съедобность - съедобный
            #print(self.name)
            self.fed = True
            print(f' {self.name}  съел  {food.name}; наелся <self.fed> = {self.fed}; '
                  f'Живой, бегает и радуется <self.alive> = {self.alive}')

        else:
            print('food.edible=',food.edible, '- не съедобный')
            # print(self.name)
            # print(food.name)
            self.alive = False
            print(f' {self.name} не стал есть  {food.name}, Остался голодный <self.fed> = {self.fed}; '
                  f'Будет жить, если срочно съест мясо <self.alive> = {self.alive}')

class Mammal(Animal): # субкласс класса Animal
    #pass
    def about(self):
        return f'Я -  {self.name} - объект класса - {Mammal.__name__}'

class Predator(Animal): # субкласс класса Animal
    #pass
    def about(self):
        return f'Я -  {self.name} - объект класса - {Predator.__name__}'

class Plant(Animal): #подкласс Animal и  Родительский класс для Flower Fruit
    edible = False # съедобность - не съедобный
    # def __init__(self, name):
    #     self.name = name

class Flower(Plant): # субкласс класса Plant
    #edible = True
    def about(self):
       return f'Я -  {self.name} - объект класса - {Flower.__name__}'

class Fruit(Plant):
    edible = True # cъедобность - съедобный
    def about(self):
        return f'Я -  {self.name} - объект класса - {Fruit.__name__}'



a1 = Predator('Волк с Уолл-Стрит ')
print('Первое животное - ', a1.name)
p1 = Flower('Цветик семицветик')
print('Еда - ', p1.name)
a1.eat(p1)

a2 = Mammal('Хатико')
print('Второе животное - ', a2.name)
p2 = Fruit('Заводной апельсин')
print('Еда - ', p2.name)
a2.eat(p2)


   ### Второй вариант

class Animal: #Родительский класс
    alive = True # живой - да
    fed = False  # накормленный - нет
    def __init__(self, name): # Конструктор имени класса
        self.name = name

    def eat(self, food): #   # Почему при таком исполнении у функции "eat" из класса Animal есть доступ
                        # к параметру edible из класса Plant, они же никак не связаны между собой ????
                        # Что означает условие - if food.edible:   ??
                        #  Как функция определяет  True и False?
        if food.edible:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Mammal(Animal): # субкласс класса Animal
    #pass
    def about(self):
        return f'Я -  {self.name} - объект класса - {Mammal.__name__}'

class Predator(Animal): # субкласс класса Animal
    #pass
    def about(self):
        return f'Я -  {self.name} - объект класса - {Predator.__name__}'

class Plant: #Родительский класс для Flower и Fruit
    edible = False # съедобный
    def __init__(self, name):
        self.name = name

class Flower(Plant): # субкласс класса Plant
    #edible = True
    def about(self):
       return f'Я -  {self.name} - объект класса - {Flower.__name__}'

class Fruit(Plant):
    edible = True
    def about(self):
        return f'Я -  {self.name} - объект класса - {Fruit.__name__}'


print(f'\n Второй вариант:')

a1 = Predator('Волк с Уолл-Стрит ')
print('Первое животное - ', a1.name)
p1 = Flower('Цветик семицветик')
print('Еда - ', p1.name)
a1.eat(p1)

a2 = Mammal('Хатико')
print('Второе животное - ', a2.name)
p2 = Fruit('Заводной апельсин')
print('Еда - ', p2.name)
a2.eat(p2)


