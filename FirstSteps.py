import math

def les1():
    print(2 + 3)
    print('Hello!!!')
    a = 145
    b = 214
    c, d = 24, 53
    pi = 3.14

    print("a + b =", a+b)
    print("c =", c)
    print("d =", d)

    print(pi)
    return()

def les2():
    a, b = map(int, input('Введите целые числа через пробел:').split())
    print(math.sqrt(pow(a, 2) + pow(b, 2)))

    a = float(input("Введите дробное число:"))
    b = a % 3
    res = b >= 0 and b < 1
    print(b, res, sep=" | ")
    return()

def les3():
    x = 435.56
    res = round(x % 1, 2) > 0.50
    print(res)

    a, b = map(int, input('Введите целые числа через пробел:').split())
    res1 = round((a / b) % 1, 3) == 0
    print(res1)
    return()
les1()
les2()
les3()

