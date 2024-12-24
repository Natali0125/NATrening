def test_function():

    def inner_function():
        a = 'Я в области видимости функции test_function'
        return a
    a = inner_function()
    print(a)



test_function()

# При вызове функции "inner_function()"
# Вне функции test_function()
#  функция inner_function() не вызывается
# #
#     Выводится ошибка:
# #  File "C:\Users\igors\PycharmProjects\PythonProject\modul_Prostr_Name.py", line 12, in <module>
# #     inner_function()
# #     ^^^^^^^^^^^^^^
# #  NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
#    test_function




