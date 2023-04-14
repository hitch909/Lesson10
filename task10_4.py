"""
Задание 4.
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

my_text = ['разработка', 'администрирование', 'protocol', 'standard']
my_text_enc = []
my_text_dec = []

for i in my_text:
    temp = str.encode(i, encoding='utf-8')
    my_text_enc.append(temp)
print(*my_text_enc)

print()

for i in my_text_enc:
    temp = bytes.decode(i, encoding='utf-8')
    my_text_dec.append(temp)
print(*my_text_dec)
