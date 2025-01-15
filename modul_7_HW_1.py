 # Модуль_7 - тема "Режимы открытия файлов"
 # Задача "Учёт товаров

class Product:
    def __init__(self, name = str,  weight = float, category = str ):
        self.name = name
        self.weght = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weght}, {self.category} '

class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

 # Метод считвыает содержимое файла и выводит информацию о содержимом файла
    def get_products(self):
        self.__file_name = 'products.txt'
        file = open(self.__file_name, 'r')
        products = file.read()
        #print(products)
        file.close()
        return products

 # Метод проверяет наличие товара в магазине и не добавляет, если таковой есть
    def add(self, *products):
        for product in products:
            if product.__str__()  not in self.get_products():
                file = open(self.__file_name, 'a')
                file.write(product.__str__() + '\n')
                file.close()
            else:
                print(f'Продукт {product.name} уже есть в магазине')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)
print(s1.get_products())
#
# Первый запуск:
# Spaghetti, 3.4, Groceries
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables
#
# Второй запуск:
# Spaghetti, 3.4, Groceries
# Продукт Potato уже есть в магазине
# Продукт Spaghetti уже есть в магазине
# Продукт Potato уже есть в магазине
# Potato, 50.5, Vegetables
# Spaghetti, 3.4, Groceries
# Potato, 5.5, Vegetables




