"""
Задание 3.
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).
Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- обязательно!!! усложните задачу, "отловив" исключение,
придумайте как это сделать
"""

text = ['attribute', 'класс', 'функция', 'type']
for i in text:
    if len(bytes(i, 'utf-8')) <= 9:
        print(f"можно записать в байтовом типе с помощью маркировки b'': {i}")
