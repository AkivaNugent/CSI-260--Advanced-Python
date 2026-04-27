math_values1 = {'one': 10, 'two': 22, 'three': 7, 'four': 45, 'five': 20}
math_values2 = [2, 4, 8, 16, 32, 64, 128]
math_values3 = [ 0, 1, 1, 2, 3, 5, 8, 13]


def mathFunction(*args, **kwargs):
    values = list(args) + list(kwargs.values())

    addition = sum(values)

    product = 0
    if values:
        product = 1

    for x in values:
        product *= x

    return addition, product


print(mathFunction(**math_values1))
print(mathFunction(*math_values2))
print(mathFunction(*math_values3))
