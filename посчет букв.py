word = input("введите слово: ")
sum_first = input("введите 1ю букву: ")
sum_second = input("введите 2ю букву: ")
symbol_count_first = 0
symbol_count_second = 0
for symbol in word:
    if symbol == sum_first:
        symbol_count_first += 1
    if symbol == sum_second:
        symbol_count_second += 1
print("колличество букв ", sum_first, "=", symbol_count_first)
print("колличество букв ", sum_second, "=", symbol_count_second)