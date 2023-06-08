def fibonacci(limit):
    n1 = 0
    n2 = 1

    if limit == 1:
        return [n1]
    else:
        result = [n1, n2]
        for i in range(2, limit):
            result.append(result[i-2]+result[i-1])
        return result


print(fibonacci(int(input('Введите количество чисел последовательности Фибоначчи: '))))
