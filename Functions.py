import re


def ex715(fn):
    '''Объявите функцию, которая имеет один параметр - вес предмета и выводит на экран сообщение (без кавычек):
    "Предмет имеет вес: x кг."
    где x - переданное значение функции.
    После объявления функции прочитайте (с помощью функции input) вещественное число и вызовите функцию с этим значением.
    Sample Input:
    12.67
    Sample Output:
    Предмет имеет вес: 12.67 кг.
    '''
    print(f"Предмет имеет вес: {fn} кг.")


def ex716(i):
    '''Объявите функцию, которая принимает список,
    находит максимальное, минимальное и сумму значений этого списка и выводит результат в виде строки (без кавычек):
    "Min = v_min, max = v_max, sum = v_sum"
    где v_min, v_max, v_sum - вычисленные значения минимального, максимального и суммы значений списка.
    После объявления функции прочитайте (с помощью функции input) список целых чисел,
    записанных в одну строку через пробел, и вызовите функцию с этим списком.
    Sample Input:
    8 11 5 -10 12 0
    Sample Output:
    Min = -10, max = 12, sum = 26
    '''
    i = list(i)
    print(f"Min = {min(i)}, max = {max(i)}, sum = {sum(i)}")

def ex717(a):
    '''Объявите функцию с двумя параметрами width и height (ширина и высота прямоугольника),
    которая выводит сообщение (без кавычек):
    "Периметр прямоугольника, равен x"
    где x - вычисленный периметр прямоугольника.
    После объявления функции прочитайте (с помощью функции input) два целых числа,
    записанных в одну строку через пробел, и вызовите функцию с этими значениями.
    Sample Input:
    8 11
    Sample Output:
    Периметр прямоугольника, равен 38
    '''
    print(f"Периметр прямоугольника, равен {2 * (a[0] + a[1])}")

def ex718(mail):
    ''' Напишите функцию, которая проверяет корректность переданного ей email-адреса в виде строки.
    Будем полагать, что адрес верен, если он обязательно содержит символы '@' и '.',
    а все остальные символы могут принимать значения: 'a-z', 'A-Z', '0-9' и '_'. Если email верен,
    то функция выводит ДА, иначе - НЕТ.
    После объявления функции прочитайте (с помощью функции input) строку с email-адресом и вызовите функцию с этим аргументом.
    Sample Input:
    sc_lib@list.ru
    Sample Output:
    ДА
    '''
    r = re.fullmatch('^[a-zA-Z0-9._-]+@[a-zA-Z]+.[a-zA-Z]*$', mail)
    if r:
        print("ДА")
    else:
        print("НЕТ")

def ex721(a):
    """Объявите функцию, которая принимает один аргумент (вещественное число), и возвращает квадрат этого числа.
    После объявления функции прочитайте (с помощью функции input) вещественное число и вызовите функциюс этим значением.
    Выведите на экран результат работы функции.
    Sample Input:
    1.5
    Sample Output:
    2.25
    """
    return a ** 2


def ex722():
    """Объявите функцию с именем is_triangle, которая принимает три стороны треугольника (целые числа) и проверяет,
    можно ли из переданных аргументов составить треугольник.
    (Напомню, что у любого треугольника длина третьей стороны всегда должна быть меньше суммы двух других).
    Если  проверка проходит, вернуть булево значение True, иначе - значение False.
    Вызывать функцию не нужно, только задать.
    Sample Input:
    3 4 5
    Sample Output:
    True
    """
    def is_triangle(a, b, c):
        return True if a + b >= c else False

    print(is_triangle(*map(int, input().split())))


def ex723():
    '''Объявите функцию с именем is_large, которая принимает строку (в качестве аргумента) и возвращает False,
    если длина строки меньше трех символов. Иначе возвращается значение True.
    Вызывать функцию не нужно, только объявить.
    Sample Input:
    Я люблю Python!
    Sample Output:
    True
    '''
    def is_large(str):
        return True if len(str) > 3 else False

    s = "Я люблю Python!"
    print(is_large(s))


def ex724():
    '''Объявите функцию для проверки числа на четность (возвращается True, если переданное число четное и False,
    если число нечетное).
После объявления функции в цикле необходимо считывать целое числовое значение (функцией input),
пока не поступит число 1. Если прочитанное значение четное (проверяется с помощью заданной функции),
то оно выводится на экран (в столбик, то есть, каждое значение с новой строки).
Sample Input:
2
-4
5
7
10
1
Sample Output:
2
-4
10
'''
    def even_num(num):
        return True if num % 2 == 0 else False

    n = 0
    while n != 1:
        n = int(input())
        if True:
            print(n)


def ex725():
    '''Объявите функцию для проверки числа на нечетность (возвращается True, если переданное число нечетное и False,
    если число четное).
После объявления функции прочитайте (с помощью функции input) список целых значений,
записанных в одну строку через пробел. И, используя генератор списков и созданную функцию,
сформируйте список из нечетных значений на основе введенного исходного списка. Результат отобразите на экране командой:
print(*lst)
где lst - сформированный список из нечетных значений.
Sample Input:
8 11 -15 3 2 10
Sample Output:
11 -15 3
'''
    def even_lst(l):
        return True if l % 2 != 0 else False

    lst = [8, 11, -15, 3, 2, 10]
    print(*[i for i in lst if even_lst(i)])


def ex726():
    '''Вводится слово в переменную tp. Если это слово RECT,
    то следует объявить функцию с именем get_sq с двумя параметрами, вычисляющую площадь прямоугольника
    и возвращающую вычисленное значение.
    (На экран она ничего не должна выводить, только возвращать значение).
    Если же введенное слово не RECT (любое другое), то объявляется функция с тем же именем get_sq,
    с одним параметром для вычисления площади квадрата (формула: a*a). Вычисленное значение возвращается функцией.
    (Она также ничего не выводит на экран).
    Примечание: в программе должна быть задана только одна функция с именем get_sq в зависимости от введенного слова.
    Вызывать функцию не нужно, только объявлять.
    Sample Input:
    RECT
    Sample Output:
    10
    '''
    tp = input().strip()
    if tp.lower() == 'rect':
        def get_sq(a, b):
            return a * b
    else:
        def get_sq(a):
            return a ** 2


def ex727():
    ''' Объявите функцию, которая принимает строку (в качестве аргумента) и возвращает False,
    если длина строки меньше 6 символов. Иначе возвращается значение True.
    После объявления функции прочитайте (с помощью функции input) список названий городов,
    записанных в одну строку через пробел. Затем, используя генератор списка и созданную функцию,
    сформируйте список из названий городов длиной не менее шести символов на основе введенного исходного списка.
    Результат отобразите на экране командой:
    print(*lst)
    где lst - итоговый сформированный список.
    Sample Input:
    Москва Уфа Пермь Самара Вологда
    Sample Output:
    Москва Самара Вологда
    '''
    def short_str(s):
        return True if len(s) > 5 else False
    lst_in = input().split()
    print(*[i for i in lst_in if short_str(i)])


def ex728():
    def str_len(str):
        return str, len(str)
    inpt = input().split()
    d = {str_len(i)[0]: str_len(i)[1] for i in inpt}
    a = sorted(d, key=lambda x: d[x])
    print(*a)


def ex729():
    '''Вводится список целых чисел в одну строчку через пробел.
    Необходимо задать функцию, которая принимает два аргумента (максимальное и минимальное значения из списка)
    и возвращает их произведение.
    Вызовите эту функцию и отобразите на экране полученное числовое значение.
    Подсказка: для передачи аргументов функции используйте функции max и min для введенного списка чисел.
    Sample Input:
    56 34 -30 22 1 4 10
    Sample Output:
    -1680
    '''
    def prod(a):
        return min(a) * max(a)


    i = list(map(int, input().split()))
    print(prod(i))

def evklid():
    """Алгоритм Евклида"""
    def nod(a, b):
        if a > b:
            a, b = b, a
        while b > 0:
            a, b = b, a % b
        return a
    print(nod(15, 121050))

def ex742():
    def get_rect_value(a, b, type=0):
        if type == 0:
            return 2 * (a + b)
        elif type == 1:
            return a * b
    print(get_rect_value(2, 2, 2))


def ex743():
    def check_password(s, chars="$%!?@#"):
        for i in range(len(chars)):
            c = s.find(chars[i])
            if c != -1:
                c = True
                break
        return True if len(s) >= 8 and c == True else False

    str = input()
    print(check_password(str))


def ex744():
    '''Объявите функцию, которая принимает строку на кириллице и преобразовывает ее в латиницу,
    используя следующий словарь для замены русских букв на соответствующее латинское написание:
t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
     'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
     'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
     'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
    Функция должна возвращать преобразованную строку.
    Замены делать без учета регистра (исходную строку перевести в нижний регистр - малые буквы).
    У функции также определить формальный параметр sep с начальным значением в виде строки "-".
    Он будет определять символ для замены пробелов в строке.
    После объявления функции прочитайте (с помощью функции input) строку
    и дважды вызовите функцию (с выводом результата ее работы на экран):
    - первый раз только со строкой
    - второй раз со строкой и именованным аргументом sep со значением '+'.
    Sample Input:
    Лучший курс по Python!
    Sample Output:
    luchshiy-kurs-po-python!
    luchshiy+kurs+po+python!
    '''
    def str_transform(s, sep="-"):
        t = {'ё': 'yo', 'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ж': 'zh',
             'з': 'z', 'и': 'i', 'й': 'y', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p',
             'р': 'r', 'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch', 'ш': 'sh',
             'щ': 'shch', 'ъ': '', 'ы': 'y', 'ь': '', 'э': 'e', 'ю': 'yu', 'я': 'ya'}
        transform = [t.get(i) if i in t else i for i in s]
        return "".join(transform).replace(" ", sep)
    i = input().lower()
    print(str_transform(i))
    print(str_transform(i, sep="+"))


def ex745():
    def html_tag(str, tag="h1", up=True):
        if up:
            tag = tag.upper()
        return f'<{tag}>{str}</{tag}>'
    print(html_tag(input()))

def ex753():
    '''Объявите функцию с именем get_even,
    которая принимает произвольное количество чисел в качестве аргументов и возвращает список,
    составленный только из четных переданных значений.
    Функцию выполнять не нужно, только определить.
    Sample Input:
    45 4 8 11 12 0
    Sample Output:
    4 8 12 0
    '''
    def get_even(*args):
        return (i for i in args if i % 2 == 0)
    print(*get_even(*map(int, input().split())))

def ex754():
    ''' Объявите функцию с именем get_biggest_city,
    которой можно передавать произвольное количество названий городов через аргументы.
    Данная функция должна возвращать название города наибольшей длины.
    Если таких городов несколько, то первый найденный (из наибольших). Программу реализовать без использования сортировки.
    Функцию выполнять не нужно, только определить.
    Sample Input:
    Питер Москва Самара Воронеж
    Sample Output:
    Воронеж
    '''
    def get_biggest_city(*cities):
        return max(cities, key=len)

    print(get_biggest_city(*map(str, input().split())))

def ex755():
    '''Объявите функцию с именем get_data_fig для вычисления периметра произвольного N-угольника.
    На вход этой функции передаются N длин сторон через аргументы.
    Дополнительно могут быть указаны именованные аргументы:
    type - булево значение True/False
    color - целое числовое значение
    closed - булево значение True/False
    width - целое значение
    Функция должна возвращать в виде кортежа периметр многоугольника
    и указанные значения именованных параметров в порядке их перечисления в тексте задания (если они были переданы).
    Если какой-либо параметр отсутствует, его возвращать не нужно (пропустить).
    Функцию выполнять не нужно, только определить.'''
    def get_data_fig(*args, **kwargs):
        res = tuple([sum(args), kwargs.get("type"), kwargs.get("color"), kwargs.get("closed"), kwargs.get("width")])
        return tuple(i for i in res if i != None)

    print(get_data_fig(5, 4, 9, 9, 9, 9, type=False, color='Yellow', closed=True, width=10))
    print(get_data_fig(5, 4, 9, 9, 9, 9, color='Yellow', type=False, closed=True, width=10))
    print(get_data_fig(5, 4, color='Yellow', type=False, closed=True))


def ex756():
    '''Вводится таблица целых чисел (см. пример ниже) размером N x N элементов (N определяется по входным данным).
    Эта таблица содержит нули, но кое-где - единицы. С помощью функции с именем verify,
    на вход которой передается двумерный список чисел, необходимо проверить,
    являются ли единицы изолированными друг от друга, то есть, вокруг каждой единицы должны быть нули.
    Рекомендуется следующий алгоритм. В функции verify производить перебор двумерного списка.
    Для каждого элемента (списка) со значением 1 вызывать еще одну вспомогательную функцию is_isolate
    для проверки изолированности единицы. То есть, функция is_isolate должна возвращать True,
    если единица изолирована и False - в противном случае.
    Как только встречается не изолированная единица, функция verify должна возвращать False.
    Если успешно доходим (по элементам списка) до конца, то возвращается значение True.
    Функцию выполнять не нужно, только определить.
    P. S. При реализации функции is_isolate не следует прописывать восемь операторов if.
    Подумайте, как это можно сделать красивее (с точки зрения реализации алгоритма).
    Sample Input:
    1 0 0 0 0
    0 0 1 0 0
    0 0 0 0 0
    0 1 0 1 0
    0 0 0 0 0
    Sample Output:
    True
    '''
    #matrix = [[1,1,1,1,1],[1,0,0,0,1],[1,0,0,0,1],[1,0,0,0,1],[0,0,0,0,0]]
    matrix = [[0,0,0],[0,0,1],[0,0,1]]
    def is_isolate(f_ind, t_ind, m):
        '''
        is_isolate: finds values beside with transmit value from verify function and return boolean values if values are the same;
        f_ind: first list index
        t_ind: nested list index
        m: matrix argument
        '''
        if m[f_ind][t_ind - 1] != 1 and m[f_ind][t_ind + 1] != 1 and \
                1 not in m[f_ind - 1][t_ind - 1: t_ind + 1] and \
                1 not in m[f_ind + 1][t_ind - 1: t_ind + 1] and len(m) == len(m[0]):
            return True

    def verify(m):
        """
        verify: adds to the input matrix nested lists with zeros at to start and end;
        adds to the input matrix nested lists zeros at to start nested every list and end;
        calls is_isolate function if value in nested list is one;
        m: matrix argument
        """
        for i in range(len(m)):
            m[i].insert(0, 0)
            m[i].append(0)
        m.insert(0, [0] * len(m[0]))
        m.insert(len(m) + 1, [0] * len(m[0]))

        for i in range(1, len(m) - 1):
            for j in range(1, len(m[i]) - 1):

                if m[i][j] == 1:
                    res = is_isolate(i, j, m)
                    if not res:
                        return False
        return True

    print(verify(matrix))


def ex757():
    '''Объявите функцию с именем str_min, которая сравнивает две переданные строки и возвращает минимальную из них
    (то есть, выполняется лексикографическое сравнение строк).
    Затем, используя функциональный подход к программированию
    (то есть, более сложные функции реализуются путем вызова более простых), реализовать еще две аналогичные функции:
    - с именем str_min3 для поиска минимальной строки из трех переданных строк;
    - с именем str_min4 для поиска минимальной строки из четырех переданных строк.
    Выполнять функции не нужно, только записать.
    '''
    def str_min(*args):
        return min(* args)

    def str_min3(*args):
        return str_min(args)

    def str_min4(*args):
        return str_min(args)

    print(str_min4("str1", "string2", "sr3", 'string_four'))

def ex764():
    lst = [*map(int, input().split())]
    lst.append(lst[-1] + 1)
    lst.remove(lst[-2])
    lst = [*range(*lst)]
    print(*lst)

def ex765():
    lst = [*map(float, input().split()), *input().split()]
    print(lst)

def ex766():
    '''
    Имеется словарь, содержащий пункты меню:
    menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
    Дополнительно вводятся еще пункты меню в виде строк в формате:
    название_1=url_1
    ...
    название_N=url_N
    Необходимо эту введенную информацию преобразовать в словарь и добавить к словарю menu,
    используя оператор распаковки для словарей. На результирующий словарь должна вести переменная menu.
    Выводить словарь не нужно, только сформировать.
    P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
    Sample Input:
    Города=about-cities
    Машины=read-of-cars
    Самолеты=airplanes
    Sample Output:
    Архив Главная Города Машины Новости Самолеты
    about-cities airplanes archive home news read-of-cars
    '''
    lst_in = ['Города=about-cities', 'Машины=read-of-cars', 'Самолеты=airplanes']
    menu = {'Главная': 'home', 'Архив': 'archive', 'Новости': 'news'}
    menu = {**menu, **dict(i.split('=') for i in lst_in)}
    #menu = {**menu, **lst_in}
    print(menu)

def ex774():
    '''Вводится список целых чисел в одну строчку через пробел. Необходимо вычислить сумму этих введенных значений,
    используя рекурсивную функцию (для перебора элементов списка) с именем get_rec_sum.
    Функция должна возвращать значение суммы. (Выводить на экран она ничего не должна).
    Вызовите эту функцию и выведите вычисленное значение суммы на экран.
    Sample Input:
    8 11 -5 4 3
    Sample Output:
    21
    '''
    N = list(map(int, input().split()))
    def get_rec_sum(nums):
        if len(nums) == 1:
            return nums[0]
        return nums[0] + get_rec_sum(nums[1:])
    a = get_rec_sum(N)
    print(a)


def ex775():
    '''
    Вводится натуральное число N. Необходимо с помощью рекурсивной функции fib_rec(N, f=[])
    (здесь N - общее количество чисел Фибоначчи; f - начальный список этих чисел)
    сформировать последовательность чисел Фибоначчи по правилу: первые два числа равны 1 и 1,
    а каждое следующе значение равно сумме двух предыдущих.
    Пример такой последовательности для первых 7 чисел: 1, 1, 2, 3, 5, 8, 13, ...
    Функция должна возвращать список сформированной последовательности длиной N.
    Вызывать функцию не нужно, только объявить.
    Sample Input:
    7
    Sample Output:
    1 1 2 3 5 8 13
    '''
    i = int(input())
    def fib_rec(N, f=[]):
        if N > 0:
            f += [1 if len(f) < 2 else f[-1] + f[-2]]
            return fib_rec(N - 1)
        else:
            return f


    a = fib_rec(i)
    print(a)


def ex776():
    '''
    Вводится целое неотрицательное число n. Необходимо с помощью рекурсивной функции fact_rec вычислить факториал числа n.
    Напомню, что факториал числа, равен: n! = 1 * 2 * 3 *...* n. Функция должна возвращать вычисленное значение.
    Вызывать функцию не нужно, только объявить со следующей сигнатурой:
    def fact_rec(n): ...
    Sample Input:
    6
    Sample Output:
    720
    '''
    i = int(input())
    def fact_rec(n):
        return (n * fact_rec(n - 1) if n > 0 else 1)

    a = fact_rec(i)
    print(a)

def ex777():
    '''
     Имеется следующий многомерный список:
    d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]
    С помощью рекурсивной функции get_line_list создать на его основе одномерный список из значений элементов списка d.
    Функция должна возвращать новый созданный одномерный список.
    (Только возвращать, выводить на экран ничего не нужно.)
    Вызывать функцию не нужно, только объявить со следующей сигнатурой:
    def get_line_list(d,a=[]): ...
    где d - исходный список; a - новый формируемый.
    '''
    d = [1, 2, [True, False], ["Москва", "Уфа", [100, 101], ['True', [-2, -1]]], 7.89]

    # def lil(l):
    #     if type(l) != list:
    #         return l
    #
    #     for i in l:
    #         lil(i)
    #         return i


    def get_line_list(d, a=[]):
        if type(d) != list:
            a.append(d)
        else:
            for i in d:
                get_line_list(i)
        return a
    print(get_line_list(d))

def ex778():
    #N = int(input())
    #a = 0
    def get_path(N):
        if N > 2:
            return get_path(N - 1) + get_path(N - 2)
        return N

    res = get_path(7)
    print(res)

def ex779():

    """Вводится список из целых чисел в одну строчку через пробел.
    Необходимо выполнить его сортировку по возрастанию с помощью алгоритма сортировки слиянием.
    Функция должна возвращать новый отсортированный список.
    Вызовите результирующую функцию сортировки для введенного списка
    и отобразите результат на экран в виде последовательности чисел, записанных через пробел.

    Подсказка. Для разбиения списка и его последующей сборки используйте рекурсивные функции.
    P. S. Теория сортировки в видео предыдущего шага. """

    #lst = [8, 11, -6, 3, 0, 1, 1]
    lst = list(map(int, input().split()))
    print(lst)

    def devision_func(lst):
        len_list = len(lst)
        res_a = lst[:int(len_list / 2)]
        res_b = lst[len_list // 2:]
        if len(res_a) > 1:
            devision_func(res_a)
        if len(res_b) > 1:
            devision_func(res_b)
        return merger_func(res_a, res_b)

    def merger_func(a, b):
        s = sorted(a + b)
        return s


    print(devision_func(lst))
   # print(merger(lst))

def ex784():
    dev_div = lambda a, b: a / b if a != 0 and b != 0 else None
    print(dev_div(1, 2))

def ex710_2():
    '''
    Используя замыкания функций, объявите внутреннюю функцию,
    которая увеличивает значение своего аргумента на некоторую величину n - параметр внешней функции с сигнатурой:
    def counter_add(n): ...
    Вызовите внешнюю функцию counter_add со значением аргумента 2 и результат присвойте переменной cnt.
    Вызовите внутреннюю функцию через переменную cnt со значением k, введенным с клавиатуры:
    k = int(input())
    Выведите результат на экран.
    Sample Input:
    5
    Sample Output:
    7
    '''

    k = int(input())
    n = 2

    def counter_add(n):
        def rise(k):
            return k + n
        return rise

    cnt = counter_add(k)
    print(cnt(n))


def ex710_3():
    '''
    Используя замыкания функций, объявите внутреннюю функцию,
    которая заключает в тег h1 строку s (s - строка, параметр внутренней функции).
    Далее, на вход программы поступает строка и ее нужно поместить в тег h1 с помощью реализованного замыкания.\
    Результат выведите на экран.
    P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
    Sample Input:
    Balakirev
    Sample Output:
    <h1>Balakirev</h1>
    '''
    str = "Python"
    def str_add():
        def tags_add(s):
            s.strip()
            s = "<h1>" + s + "</h1>"
            return s
        return tags_add


    cnt = str_add()
    print(cnt(str))


def ex710_4():
    """Используя замыкания функций, объявите внутреннюю функцию, которая заключает строку s
    (s - строка, параметр внутренней функции) в произвольный тег, содержащийся в переменной tag - параметре внешней функции.

    Далее, на вход программы поступают две строки: первая с тегом, вторая с некоторым содержимым.
    Вторую строку нужно поместить в тег из первой строки с помощью реализованного замыкания. Результат выведите на экран.
    P. S. Пример добавления тега h1 к строке "Python": <h1>Python</h1>
    Sample Input:
    div
    Сергей Балакирев
    Sample Output:
    <div>Сергей Балакирев</div>
    """

    str = "Python"
    tag = "div"

    def str_add(tag):
        def tags_add(s):
            nonlocal tag
            s.strip()
            s = f"<{tag}>" + s + f"</{tag}>"
            return s

        return tags_add

    cnt = str_add(tag)
    print(cnt(str))


def ex710_5():
    """Используя замыкания функций, объявите внутреннюю функцию, которая преобразует строку из списка целых чисел,
    записанных через пробел, либо в список, либо в кортеж. Тип коллекции определяется параметром tp внешней функции.
    Если tp = 'list', то используется список, иначе (при другом значении) - кортеж.
    Далее, на вход программы поступают две строки: первая - это значение для параметра tp;
    вторая - список целых чисел, записанных через пробел.
    С помощью реализованного замыкания преобразовать эти данные в соответствующую коллекцию.
    Результат вывести на экран командой (lst - ссылка на коллекцию):
    print(lst)
    Sample Input:
    list
    -5 6 8 11 0 111 -456 3
    Sample Output:
    [-5, 6, 8, 11, 0, 111, -456, 3]
    """
    def list_type(tp="tuple"):
        def change_input(l):
            return list(map(int, l.split())) if tp == "list" else tuple(map(int, l.split()))
        return change_input

    tp = "tuple"
    lst = "-5 6 8 11 0 111 -456 3"

    c = list_type(tp)
    print(c(lst))

def ex711_1():
    """Объявите функцию с именем get_sq, которая вычисляет площадь прямоугольника по двум параметрам:
    width и height - ширина и высота прямоугольника. И возвращает результат (сама ничего на экран не выводит).
    То есть, функция имеет сигнатуру:
    def get_sq(width, height): ...
    Определите декоратор func_show для этой функции, который отображает результат на экране в виде строки (без кавычек):
    "Площадь прямоугольника: <значение>"
    Вызывать функцию и декоратор не нужно, только объявить. Применять декоратор к функции также не нужно."""
    w = 8
    h = 11
    def func_show(get_sq):
        def wrapper(w, h):
            print(f'Площадь прямоугольника: {get_sq(w, h)}')
        return wrapper

    def get_sq(width, height):
        return width * height


    f = func_show(get_sq)
    f(w, h)




def main():
    #ex715(float(input()))
    #ex716(map(int, input().split()))
    #ex717(list(map(int, input().split())))
    #ex718(input())
    #print(ex722(float(input())))
    #evklid()
    #ex765()
    ex711_1()


if __name__ == '__main__':
    main()