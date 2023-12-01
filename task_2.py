# Дана строка. Указать те слова, которые содержат хотя бы одну букву "к"
str=input("Введите строку").strip().split(" ")
print(str)
new_set=set(str)
print(new_set)
for item in new_set:
    if "к" in item:
        print(item)
    else:
        print("Нет")