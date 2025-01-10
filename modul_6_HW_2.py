class Vehicl:

    __COLOR_VARIANTS = ['Синий', 'Зеленый', 'Мята', 'Белый', 'Желтый']
    # owner = ''
    # __model = ''
    # __color = ''
    # __engine_power = int

    # self._Vehicl__model

    def __init__(self, owner, __model, __color, __engine_power = 0):
        self.owner = owner
        self.__model = __model
        self.__color = __color
        self.__engine_power = __engine_power

    # Возвращает строку: "Модель: <название модели транспорта
    def get_model(self):
        return f'Модель: {self.__model}'

    # Возвращает строку: "Мощность двигателя: <мощность>"
    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

     # распечатывает результаты методов в том же порядке:
     # get_model, get_horsepower, get_color; а так же владельца в конце в формате: Владелец: <имя>
    def print_info(self):
        print(f' >{self.get_model()}\n{self.get_horsepower()}\n{self.get_color()}\nВладелец: {self.owner}')

    def set_color(self,  new_color = str):
        # if new_color.lower() in map(str.lower, self.__COLOR_VARIANTS):
        #     self.__color = new_color
        # else:
        #     print('Нельзя сменить цвет на <новый цвет>')

        if new_color.lower() in list(map(str.lower, self.__COLOR_VARIANTS)):
            self.__color = new_color.upper()
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicl):
    __PASSENGERS_LIMIT = 5
    COLOR_VARIANTS = ['new1', 'new2', 'new3']

#
# vehicle1 = Vehicl('Fedos', 'Toyota Mark II', 'blue', 500)
# vehicle1.print_info()
#
# vehicle2 = Sedan('Natalya', 'Renolt Duster', 'Black', 250)
#
# vehicle2.print_info()
#
# vehicle2.owner = 'Andrey'
# vehicle2.__color = 'whyte'
# vehicle2.print_info()
# # vehicle2.__PASSENGERS_LIMIT = 6
# # print(vehicle2.__PASSENGERS_LIMIT)
# vehicle2.set_color('МяТа')
# vehicle2.print_info()
# vehicle1.set_color('Черый')
# vehicle1.print_info()


# Текущие цвета __COLOR_VARIANTS = ['Синий', 'Зеленый', 'Мята', 'Белый', 'Желтый']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)




# Изначальные свойства

vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('BLACK')
vehicle1.set_color('ЗЕЛенЫЙ')

vehicle1.owner = 'New Owner'

# Проверяем что поменялось

vehicle1.print_info()
