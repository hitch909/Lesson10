"""
Задание 1.
Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode (НО НЕ В БАЙТЫ!!!)
и также проверить тип и содержимое переменных.
*Попытайтесь получить кодовые точки без онлайн-конвертера!
без хардкода!
Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

word1 = 'разработка'
word2 = 'сокет'
word3 = 'декоратор'
print(word1, type(word1), word2, type(word2), word3, type(word3))

'''шестнадцатеричное представление в виде str. Без hex() тип получается bytes
   word1_1 = word1.encode('unicode_escape').hex()    
   print(type(word1_1), word1_1)'''

word_123 = ['разработка', 'сокет', 'декоратор']
for i in word_123:
    print(type(i))
    print(i.encode('unicode_escape').hex())
