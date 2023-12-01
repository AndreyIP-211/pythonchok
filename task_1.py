# Дана строка. Подсчитать сколько различных символов встречается в ней.
# вывести из на экран
str=input("Введите строку")
new_set=set(str)
if " " in new_set:
    new_set.remove(" ")
print(len(new_set))