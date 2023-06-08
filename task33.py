def symbol_counter(string):
    result = {}
    for n in string:
        symbol_count = 0
        for b in string:
            if n == b:
                symbol_count += 1
            else:
                pass
        result[n] = symbol_count
    return result


print(symbol_counter(str(input('Введите текст:'))))
