# операции над множествами
first_set = {3, 2}
second_set = {3, 4, 5, 2}

#   объединение множеств    a.union(b)
#   пересечение множеств    a.intersection(b)
#   пересечение множеств и сохранение данных в исходное множество    a.intersection_update(b)
#   разность множеств    a.difference(b)
#   разность множеств и сохранение данных в исходное множество    a.difference_update(b)
#   симметрическая разность множеств    a.symmetric_difference(b)
#   симметрическая разность множеств  и сохранение данных в исходное множество  a.symmetric_difference(b)
#   является подмножеством (возвращает bool)   a.issubset(b)
#   является подмножеством, но множества не совпадают (возвращает bool)   a<b
#   включает в себя множество (возвращает bool)  a.issuperset(b)
#   включает в себя множество, но множества не совпадают (возвращает bool)  a>b

print(first_set.union(second_set))
print(first_set.intersection(second_set))
print(first_set.intersection_update(second_set))
print(first_set)
print(first_set.difference(second_set))
print(first_set.difference_update(second_set))
print(first_set)
print(first_set.symmetric_difference(second_set))
print(first_set.symmetric_difference_update(second_set))
print(first_set)
print(first_set.issubset(second_set))
print(first_set.issuperset(second_set))
