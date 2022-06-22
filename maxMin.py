def max2(x, y):
    if x > y:
        return x
    return y


def max3(x, y, z):
    return max2(x, max2(y, z))


def max6(x, y, z, i, u, o):
    return max2(max3(x, y, z), max3(i, u, o))


result = max6(89, 100, 679, 77, 44, 678)

print(result)
print('привет')
