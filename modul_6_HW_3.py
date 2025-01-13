class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    # Объкт класса Animal и атрибутами _cords и speed
    def __init__(self, speed):
        self.speed = speed
        _cords = [0, 0, 0]
        # self._cords = _cords
        # print(_cords)
        # print(_cords[2])
        # print(self._cords)

    # метод меняет соответствующие кооординаты в _cords на dx, dy и dz
    def move(self, dx, dy, dz): #_cords
        self._cords = [dx * self.speed, dy * self.speed, dz * self.speed]
        if self._cords[2] < 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0

    #
    def get_cords(self): #  который выводит координаты в формате: "X:< >, Y:< >,  Z:< >"
        return print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, i'm peaceful :)")
        if self._DEGREE_OF_DANGER >= 5:
            print("Be careful, i'm attacking you 0_0")

    # методьвыводит строку со звуком sound
    def speak(self):
        sound = ''
        self.sound = sound
        print(self.sound)

# Класс описывающий птиц. Наследуется от Animal
class Bird(Animal):
    _DEGREE_OF_DANGER = 0
    beak = True #наличие клюва
    sound = 'чик-чирик'

    def lay_eggs(self):
        import random
        eggs = random.randint(1, 4) # случайное число от 1 до 4
        print(f"Here are(is) {eggs} eggs for you")#выводит строку "Here are(is)
                                                # <случайное число от 1 до 4> eggs for you"


class AquaticAnimal(Animal): #Класс описывающий плавающего животного. Наследуется от Animal.
    _DEGREE_OF_DANGER = 3

    # метод должен всегда уменьшает координату z в _coords
    def dive_in(self, dz):
        # Скорость движения при нырянии уменьшается в 2 раза
        self._cords[2] = int(self._cords[2] - (int(abs(dz)) * (self.speed / 2)))

class PoisonousAnimal(Animal): #класс описывающий ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8.

class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def speak(self):
        sound = 'Click-click-click'
        return print(sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()

# Вывод на консоль:
# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you # Число может быть другим (1-4)

#print(Duckbill.__mro__)

