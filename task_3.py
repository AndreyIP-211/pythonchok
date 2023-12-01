# Задается текст. Словом  текста считается последовательность
# непробельных символов, идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.
# Определите, сколько различных слов содержится в этом тексте.
import string

str=input("Введите строку").strip().split()

new_set=set()
print(new_set)
for item in str:
    item=item.lower()
    item=item.strip(string.punctuation)
    new_set.add(item)
print(new_set)
