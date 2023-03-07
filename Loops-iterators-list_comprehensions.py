import random
import sys
import math
### Циклы, итераторы и генераторы списков ###
### Цикл While ###
def enter_pass():
    true_pass = "password"
    ps = ""
    try_num = 0
    while ps != true_pass and try_num < 5:
        ps = input("Enter Password: ")
        if ps != true_pass:
            print(f"Осталось попыток: {4 - try_num}")
        try_num = try_num + 1

    if try_num > 4:
        print("Попыток больше нет!!!")
    else:
        print("### ВХОД ВЫПОЛНЕН ###")
    return 0
# enter_pass()

def bye_books():
    book = float(input("Enter book price: "))
    c = 0
    while c < 10:
        c += 1
        print(round(book * c, 1), end=" ")
    return 0
#bye_books()

def ex513():
    n = 8
    m = 0
    sum = 0
    while n > 0:
        sum = m + 1 / n + sum
        n -= 1
    print(round(sum, 3))
    return 0
#ex513()

def ex514():
    n = ""
    m = 0
    while n != 0:
        n = int(input("Enter int number: "))
        m = n + m
    print(m)
    return 0
#ex514()

def strings_defisz():
    str = input()
    while str.count("--") != 0:
        str = str.replace("--", "-")
    print(str)
    return 0
#strings_defisz()

def ex516():
    n = input()
    lst = list(n)
    m = 0
    s = 1
    while m != len(lst):
        s = int(lst[m]) * s
        m = m + 1
    print(s)
    return 0
#ex516()

def Fibanachi():
    n = int(input("Enter Number: "))
    fib1 = 1
    fib2 = 0
    i = 0
    while i < n - 1:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i += 1
        print(fib2, end=' ')
    return 0
#Fibanachi()

def ameba():
    """Одноклеточная амеба каждые 3 часа делится на 2 клетки.
    Определить, сколько клеток будет через n часов (n - целое положительное число, вводимое с клавиатуры).
    Считать, что изначально была одна амеба.
    Результат вывести на экран. Задачу необходимо решить с использованием цикла while."""
    n = int(input("Enter hours: "))
    a = 1
    while n >= 3:
        a = a * 2
        n = n - 3
    print(a)
    return 0
#ameba()

def vklad():
    """Гражданин 1 января открыл счет в банке, вложив 1000 руб.
    Каждый год размер вклада увеличивается на 5% от имеющейся суммы.
    Определить сумму вклада через n лет (n - целое положительное число, вводимое с клавиатуры).
    Результат округлить до сотых и вывести на экран. Программу реализовать при помощи цикла while."""
    y = int(input("Enter int num: "))
    v = 1000
    while y > 0:
        p = v * 0.05
        v = v + p
        y -= 1
    print(round(v, 2))
    return 0
#vklad()

def self_lst():
    '''Вводятся два натуральных четных числа n и m в одну строчку через пробел, причем n < m.
    Напечатать все нечетные числа из интервала [n, m]. Задачу решить без применения условного оператора.
    Результат вывести на экран в виде строки чисел, записанных через пробел.
    Программу реализовать при помощи цикла while.'''
    n, m = map(int, input().split())
    n = n - 1
    while n < m - 1:
        n += 2
        print(n, end=" ")
    return 0
#self_lst()

def ex5113():
    ''' Составить программу поиска всех трехзначных чисел,
    которые при делении на 47 дают в остатке 43 и кратны 3.
    Вывести найденные числа в строчку через пробел. Программу реализовать при помощи цикла while.'''
    i = 100
    while i < 1000:
        if i % 47 == 43 and i % 3 == 0:
            print(i, end=" ")
        i += 1
    return 0
#ex5113()

### Операторы break, continue, else ###

# break - досрочное завершение цикла;
# continue - пропуск одной итерации цикла;
# else - выполнение блока операторов после завершения цикла
'''while <условие цикла>: (заголовок)
        <оператор 1>
        <оператор 2>
            ...     
        <оператор N>
        (тело цикла)
    else:
        блок операторов после завершения цикла
        (блок выполняется после штатного завершения цикла)
    
    последующие операторы
        '''
def contlst():
    '''Имеется одномерный список длиной 10 элементов, состоящий из нулей:
    p = [0] * 10
    На каждой итерации цикла пользователь вводит целое число - индекс элемента списка p,
    по которому записывается значение 1, если ее там еще нет. Если же 1 уже проставлена,
    то список не менять и снова запросить у пользователя очередное число.
    Необходимо расставить так пять единиц в список. (После этого цикл прерывается).
    Программу реализовать с помощью цикла while и с использованием оператора continue,
    когда 1 не может быть добавлена в список.
    Результат вывести на экран в виде последовательности чисел, записанных через пробел.'''

    p = [0] * 10
    while p.count(1) < 5:
        a = int(input("Введите индекс элемента списка: "))
        if p[a] != 0:
            continue
        p[a] = 1
    print(*p)
    return 0
#contlst()

def contsum():
    '''На каждой итерации цикла вводится целое число. Необходимо подсчитать произведение только положительных чисел,
    до тех пор, пока не будет введено значение 0. Реализовать пропуск вычислений с помощью оператора continue,
    а также использовать цикл while. Результат произведения вывести на экран.'''
    a = ""
    sum = 1
    while a != 0:
        a = int(input("Enter number: "))
        if a <= 0:
            continue
        sum *= a
    print(sum)
    return 0
#contsum()

def cities_name():
    '''Вводится список названий городов в одну строчку через пробел.
    Определить, что в этом списке все города имеют длину более 5 символов.
    Реализовать программу с использованием цикла while и оператора break.
    Вывести ДА, если условие выполняется и НЕТ - в противном случае.'''

    cit_list = input().split() #List of cities
    i = 0
    a = 1
    while i < len(cit_list):
        if len(cit_list[i]) < 5:
            break
        i = i + 1
    else:
        a = 0
    if a == 1:
        print("NO")
    else:
        print("YES")
    return 0
#cities_name()

def stud_names():
    '''Вводится список имен студентов в одну строчку через пробел.
    Определить, что хотя бы одно имя в этом списке начинается и заканчивается на ту же самую букву (без учета регистра).
    Реализовать программу с использованием цикла while и оператора break.
    Вывести ДА, если условие выполняется и НЕТ - в противном случае.'''
    names = input()
    lst = list(names.lower().split())
    print(lst)
    i = len(lst)
    while i > 0:
        if lst[i - 1][0] == lst[i - 1][-1]:
            print("ДА")
            break
        i = i - 1
    else:
        print("НЕТ")
    #print(lst[0][-1])
    #print(lst[0][0])
    return 0
#stud_names()

def ex526():
    '''Вводится натуральное число n (то есть, целое положительное).
    В цикле перебрать все целые числа в интервале [1; n] и сформировать список из чисел,
    кратных 3 и 5 одновременно. Вывести полученную последовательность чисел в виде строки через пробел,
    если значение n меньше 100. Иначе вывести на экран сообщение "слишком большое значение n" (без кавычек).
    Использовать в программе оператор else после цикла while.'''
    n = int(input("Введите натуральное число: "))
    i = 0
    while i < n and n < 100:
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            print(i, end=" ")
            continue
    else:
        if n >= 100:
            print("слишком большое значение n")
    return 0
#ex526()

def ex517():
    '''Вводится натуральное число n. Вывести первое найденное натуральное число
    (то есть, перебирать числа, начиная с 1), квадрат которого больше значения n.
    Реализовать программу с использованием цикла while.'''
    n = int(input())
    i = 0
    while i * i < n:
        i += 1
    print(i)
    return 0
#ex517()

def skier():
    '''(На использование цикла while). Начав тренировки, лыжник в первый день пробежал 10 км.
    Каждый следующий день он увеличивал пробег на 10 % от пробега предыдущего дня.
    Определить в какой день он пробежит больше x км (натуральное число x вводится с клавиатуры).
    Результат (искомый день) вывести на экран.'''
    fd = 10
    day = 1
    xkm = int(input())
    while fd < xkm:
        fd = fd + fd * 0.1
        day += 1
        #print(day, fd)
    print(day)
    return 0
#skier()

def booksnames():
    '''(На использование цикла while). Вводятся названия книг (каждое с новой строки).
    Удалить из введенного списка все названия, состоящие из двух и более слов (слова в названиях разделяются пробелом).
    Результат вывести на экран в виде строки из оставшихся названий через пробел.

    P. S. Для считывания списка целиком в программе уже записаны начальные строчки'''
    bl = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая дама', 'Колобок']
    i = 0
    while i < len(bl):
        if ' ' in bl[i]:
            print(bl[i])
            bl.pop(i)
            continue
        i += 1
    print(bl)
    return 0
#booksnames()

### Оператор цикла for и функция range ###
### Оператор for ###
'''
for <переменная> in <итерируемый объект>:
    Оператор 1
    Оператор 2
       ...
    Оператор N
'''
def ex_for():
    d = [1, 2, 3, 4, 5, 6]
    for x in d:
        print(x)
    return 0
#ex_for()
### Функция range() ###
# range(start, stop, step)
def ex_range():
    a = list(range(5))
    b = list(range(0, 10, 2))
    c = list(range(-10, -5))
    d = list(range(-10, -20, -1))
    e = list(range(5, 0, -1))
    rng = [a, b, c, d, e]
    for x in rng:
        print(x)
    return 0
#ex_range()

def cities_ch():
    """
    Вводятся названия городов в одну строчку через пробел.
    Необходимо преобразовать входные данные в список.
    Затем, перебрать его циклом for и заменить значения элементов на длину названия соответствующего города.
    Результат вывести на экран в виде последовательности чисел через пробел в одну строчку.
    INPUT: Москва Уфа Караганда Тверь Минск Казань
    OUTPUT: 6 3 9 5 5 6
    """
    cities = list(input('Введите названия городов через пробел: ').split())
    #print(cities)
    for x in cities:
        print(len(cities[cities.index(x)]), end=" ")
    return 0
#cities_ch()
def divisor():
    '''Вводится натуральное число n. С помощью цикла for найти все делители этого числа.
    Найденные делители выводить сразу в столбик без формирования списка.'''
    num = int(input("ENTER NUMBER: "))
    d = 1
    dlist = []
    while d <= num:
        dlist.append(d)
        d += 1
    for x in dlist:
        if num % x == 0:
            print(x)
    print(dlist)
    return 0
#divisor()

def ex538():
    '''
    Вводится натуральное число n. С помощью цикла for определить,
    является ли оно простым (то есть, делится нацело только на само себя и на 1).
    Вывести на экран ДА, если n простое и НЕТ - в противном случае.
    '''
    num = int(input())
    l = []
    for x in range(1, num + 1):
        l.append(num % x)
    print(l)
    if 0 in l[1:-1]:
        print("НЕТ")
    else:
        print("ДА")
    return 0
#ex538()

def ex539():
    '''
    Вводится список названий городов в одну строчку через пробел.
    Перебрать все эти названия с помощью цикла for и определить,
    начинается ли название следующего города на последнюю букву предыдущего города в списке.
    Если последними встречаются буквы 'ь', 'ъ', 'ы', то берется следующая с конца буква.
    Вывести на экран ДА, если последовательность удовлетворяет этому правилу и НЕТ - в противном случае.

    Sample Input: Москва Астрахань Новгород Димитровград Душанбе
    Sample Output: ДА
    '''
    cities = list(input('Введите названия городов через пробел: ').lower().split())
    l = []
    a = -1
    for x in cities[0:-1]:
        if cities[cities.index(x)][a] == 'ь' or cities[cities.index(x)][a] == 'ъ' or cities[cities.index(x)][a] == 'ы':
            if cities[cities.index(x)][a - 1] == cities[cities.index(x) + 1][0]:
                l.append(1)
        elif cities[cities.index(x)][a] == cities[cities.index(x) + 1][0]:
            l.append(1)
        else:
            l.append(0)
    if 0 in l:
        print("НЕТ")
    else:
        print("ДА")
    return 0
#ex539()

def ex5311():
    '''
    Вводится натуральное число n. Вычислить сумму всех натуральных чисел меньше n,
    которые кратны или 3 или 5. Результат (сумму) вывести на экран.
    Пример: n = 10, имеем числа: 3, 5, 6, 9. Их сумма равна 23.
    '''
    n = int(input())
    nl = list(range(1, n))
    res = 0
    print(nl)
    for x in nl:
        if x % 3 == 0 or x % 5 == 0 and x < n:
            print(x)
            res += x
        else:
            continue
    print(res)
    return 0
#ex5311()

#Функция enumerate() вернет кортеж, содержащий отсчет от start и значение, полученное из итерации по объекту.

def ex541():
    '''
    Вводится строка. Необходимо найти все индексы фрагмента "ра" во введенной строке.
    Вывести в строку через пробелы найденные индексы.
    Если этот фрагмент ни разу не будет найден, то вывести значение -1.
    '''
    str = input()
    if 'ра' not in str:
        print(-1)
    else:
        for i, d in enumerate(str.lower()):
            if d == 'р' and str[i + 1] == 'а':
                print(i, end=" ")
    return 0

#ex541()

def ex542():
    '''
    Вводится строка с номером телефона. Ожидается формат ввода:
    +7(xxx)xxx-xx-xx
    где x - это цифра. Размер введенных символов считается верным
    (то есть, не может быть, чтобы отсутствовала какая-либо цифра или была лишняя).
    Необходимо проверить, что введенная строка соответствует этому формату.
    Вывести ДА, если соответствует и НЕТ - в противном случае.

    Sample Input:
    +7(123)456-78-99
    Sample Output:
    ДА
    '''
    pn = input()
    tel = ''
    if len(pn) == 16:
        #
        if pn[0] == '+' and pn[1] == '7' and pn[2] == '(' and pn[6] == ')' and pn[10] == '-' and pn[13] == '-':
                for i, d in enumerate(pn):
                    if pn[i] == '+' or pn[i] == '(' or pn[i] == ')' or pn[i] == '-':
                        a = 1
                    else:
                        tel += d
    if tel.isdigit():
        print("ДА")
    else:
        print("НЕТ")
    return 0
#ex542()

def ex543():
    '''
     В виде строки записано арифметическое выражение, например:
    "10 + 25 - 12"
    или
    "10 + 25 - 12 + 20 - 1 + 3"
    и т. д. То есть, количество действий может быть разным.
    Необходимо выполнить вычисление и результат отобразить на экране.
    Полагается, что в качестве арифметических операций здесь используется только сложение (+) и вычитание (-),
    а в качестве операндов - целые неотрицательные числа.
    Следует учесть, что эти операторы могут быть записаны как с пробелами, так и без них.
    '''
    l = 1
    expr = input()
    strres = expr.strip().replace(" ", "").replace("+", "_+_").replace("-", "_-")
    #strres = expr.replace(" ", "").replace("+", "_+_").replace("-", "_-")
    expr = list(strres.split("_"))
    for i, item in enumerate(expr):
        if item == "+":
            expr.pop(i)
    for i, item in enumerate(expr):
        expr[i] = int(item)
        expr.sort()
    print(sum(expr))
    return 0
#ex543()

def ex544():
    '''
    Вводится список в виде целых чисел в одну строку через пробел.
    Сначала нужно сформировать список из введенной строки.
    Затем, каждый элемент этого списка продублировать один раз.
    Результат отобразить на экране в виде строки полученных чисел, записанных через пробел.
    '''
    s = list(map(int, input().split()))
    for i, v in enumerate(s):
        if s.count(v) == 1:
            s.insert(i + 1, v)
    print(*s)
    return 0
#ex544()

def ex545():
    '''
    Вводится список в виде вещественных чисел в одну строку через пробел.
    С помощью цикла for необходимо найти наименьшее значение в этом списке.
    Полученный результат вывести на экран.
    Реализовать программу без использования функции min, max и сортировки.
    '''
    lst = list(map(float, input().split()))
    i = 0
    lst.sort()
    print(lst[0])
    # for x, item in enumerate(lst):
    #     #print(item)
    #     while i < len(lst):
    #         if lst[x] < lst[x + i]:
    #             a = lst[x]
    #         i += 1

    #print(a)

    return 0
#ex545()

def ex546():
    '''
    Вводится список в виде вещественных чисел в одну строку через пробел.
    Сначала нужно сформировать список из введенной строки.
    Затем, все отрицательные значения в этом списке заменить на -1.0.
    Результат вывести на экран в виде строки чисел через пробел.
    Программу следует реализовать с использованием функции enumerate.
    '''
    lst = list(map(float, input().split()))
    for i, item in enumerate(lst):
        if item < 0:
            lst[i] = -1.0
    print(*lst)
    return 0
#ex546()



# 5.5 Итератор и итерируемые объекты. Функции iter и next

"""Основное назначение итератора -  это упрощение навигации по элементам объекта, 
который, как правило, представляет собой некоторую коллекцию (список, словарь и т.п.)."""

def ex551():
    """
    Вводится список городов в одну строчку через пробел.
    Необходимо создать итератор для этого списка и с помощью итератора вывести на экран в столбик первые два значения
    (названия городов).
    """
    str = input().split()
    it = iter(str)
    i = 0
    while i < 2:
        print(next(it))
        i += 1
    return 0
#ex551()

def ex551_1():
    i = 0
    lst = []
    while i < 15:
        lst.append(random.randrange(999999))
        i += 1
    print(lst)
    it = iter(lst)
    for j in range(len(lst)):
        print(next(it))

ex551_1()
def ex552():
    '''
    Вводится строка. Нужно создать итератор для перебора символов этой строки.
    Затем, перебрать через созданный итератор все символы до первого пробела.
    В процессе перебора символы выводить на экран в одну строчку друг за другом (без пробелов).
    Гарантируется, что во введенной строке имеется хотя бы один пробел.
    '''
    s = input()
    t = iter(s)
    for i in s:
        n = next(t)
        if n != " ":
            print(n, end="")
        else:
            break
    return 0
#ex552()

def ex553():
    '''
    Вводится четырехзначное целое положительное число.
    Подумайте, как можно определить итератор для перебора его цифр.
    Выведите цифры этого введенного числа (с помощью итератора) в одну строчку через пробел.
    '''
    n = int(input())
    x = [a for a in str(n)]
    t = iter(x)
    for i in x:
        print(next(t), end=" ")
    return 0
#ex553()

# 5.6 Вложенные циклы
def ex561():
    '''
    Вводится натуральное число N (то есть, положительное, целое).
    Требуется создать двумерный (вложенный) список размером N x N элементов, состоящий из всех единиц,
    а затем, в последний столбец записать пятерки.
    Вывести этот список на экран в виде таблицы чисел, как показано в примере ниже.

    P.S. Будьте внимательны в конце строк пробелов быть не должно!
    Sample Input:
    4
    Sample Output:
        1 1 1 5
        1 1 1 5
        1 1 1 5
        1 1 1 5
    '''
    l = []
    n = int(input())
    for i in list(range(n)):
        if i == n - 1:
            l.append(5)
        else:
            l.append(1)
    for j in list(range(n)):
        print(*l)
    return 0
#ex561()

def ex562():
    '''
    Вводится список из URL-адресов (каждый с новой строки). Требуется в них заменить все пробелы на символ дефиса (-).
    Следует учесть, что может быть несколько подряд идущих пробелов.
    Результат преобразования вывести на экран в виде строк из URL-адресов.
    P. S. Для считывания списка целиком в программе уже записаны начальные строчки.

    Sample Input:
    django chto  eto takoe    poryadok ustanovki
    model mtv   marshrutizaciya funkcii  predstavleniya
    marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya

    Sample Output:
    django-chto-eto-takoe-poryadok-ustanovki
    model-mtv-marshrutizaciya-funkcii-predstavleniya
    marshrutizaciya-obrabotka-isklyucheniy-zaprosov-perenapravleniya
    '''
    lst = ['django chto  eto takoe    poryadok ustanovki',
           'model mtv   marshrutizaciya funkcii  predstavleniya',
           'marshrutizaciya  obrabotka isklyucheniy       zaprosov perenapravleniya']
    for i, item in enumerate(lst):
        lst[i] = lst[i].replace(" ", "-")
        lst[i] = lst[i].replace("---", "-").replace("--", "-")
        for j, item2 in enumerate(lst):
            lst[i] = lst[i].replace("--", "-")

        print(lst[i])
    return 0
#ex562()

def ex563():
    '''
    Вводится натуральное число n. Необходимо найти все простые числа, которые меньше этого числа n,
    то есть, в диапазоне [2; n). Результат вывести на экран в строчку через пробел.

    Sample Input:
        11
    Sample Output:
        2 3 5 7
    '''
    n = int(input())
    lst = []
    for i in range(2, n):
        for j in range(2, i):
            lst.append(i % j)
        if 0 not in lst:
            print(lst, i)
        lst.clear()

    return 0
#ex563()

def ex564():
    '''
    Вводится двумерный список размерностью 5 х 5 элементов, состоящий из нулей и, в некоторых позициях,
    единиц (см. пример ввода ниже). Требуется проверить, не касаются ли единицы друг друга по горизонтали,
    вертикали и диагонали.vТо есть, вокруг каждой единицы должны быть нули.
    Если проверка проходит вывести ДА, иначе - НЕТ.
     Sample Input:
        1 0 0 0 0
        0 0 1 0 1
        0 0 0 0 0
        0 1 0 1 0
        0 0 0 0 0
    '''
    matrix = [[1, 0, 0, 0, 0], [0, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0]]
    #for x in range(len(matrix)):
    matrix.insert(0, [0] * len(matrix))
    matrix.append([0] * len(matrix[1]))
    for x in range(len(matrix)):
        matrix[x].insert(0, 0)
        matrix[x].append(0)
        l = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
                if matrix[i][j - 1] != 1 and matrix[i][j + 1] != 1 and matrix[i - 1][j] != 1 and matrix[i + 1][j] != 1 and matrix[i - 1][j - 1] != 1 and matrix[i - 1][j + 1] != 1 and matrix[i + 1][j - 1] != 1 and matrix[i - 1][j + 1] != 1:
                   l.append(1)
                else:
                    l.append(0)
    if 0 in l:
        print("НЕТ")
    else:
        print("ДА")

    #print(matrix)
    return 0
#ex564()

def ex565():
    '''
    Вводится двумерный список размерностью 5 х 5 элементов, состоящий из целых чисел (пример ввода см. ниже).
    Проверьте, является ли этот двумерный список симметричным относительно главной диагонали.
    Главная диагональ — та, которая идёт из левого верхнего угла двумерного массива в правый нижний.
    Выведите на экран ДА, если матрица симметрична и НЕТ - в противном случае.
    '''
    lst_in = [[2, 3, 4, 5, 6], [3, 2, 7, 8, 9], [4, 7, 2, 0, 4], [5, 8, 0, 2, 1], [6, 9, 4, 1, 2]]
    a = 'ДА'
    for i in range(len(lst_in)):
        for j in range(i + 1, len(lst_in)):
            if lst_in[i][j] == lst_in[j][i]:
                continue
            else:
                a = "НЕТ"
                break
    print(a)
    return 0
#ex565()
def ex566():
    '''
    Вводится список целых чисел в одну строку через пробел.
    Необходимо выполнить его сортировку выбором по возрастанию (неубыванию).
    Вначале мы рассматриваем первый элемент списка и ищем второй минимальный относительно первого элемента (включая и его).
    На рисунке - это последний элемент со значением -1. Затем, меняем местами первый и последний элементы.
    Переходим ко второму элементу списка и повторяем эту же процедуру,
    но относительно второго элемента (то есть, первый уже не рассматриваем).
    На рисунке минимальный элемент - это 2, поэтому менять местами здесь ничего не нужно.
    Переходим к 3-му элементы со значением 6. Относительно него находим минимальный элемент - это 3. Меняем их местами.

    Вот идея алгоритма сортировки выбором. Реализуйте его для вводимого списка целых чисел.
    Результат выведите в виде списка чисел одну строку через пробел.
    '''
    lst = [8, 11, -53, 2, 10, 11]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] >= lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
            else:
                continue
    print(*lst)
    return 0
#ex566()

def ex567():
    '''
    Вводится список целых чисел в одну строку через пробел.
    Необходимо выполнить его сортировку по возрастанию (неубыванию) методом всплывающего пузырька.
    При первом проходе перебираем все соседние пары элементов и если значение предыдущего элемента (слева) больше значения следующего (справа),
    то они меняются местами. (На рисунке 3 и 2 меняются местами). Следующая пара - это 3 и 6.
    Они уже выстроены по возрастанию, поэтому ничего не делаем и переходим к следующей паре 6 и -1.
    Меняем значения местами и видим, что на последнем месте находится максимальное значение 6, что нам и нужно.

    При втором проходе делаем все то же самое, но доходим до предпоследнего элемента,
    так как последнее значение 6 уже отсортировано. На третьем проходе исключаем уже последние два элемента и так далее.
    То есть, в этом алгоритме достаточно сделать N-1 проходов, где N - длина списка.

    Вот идея алгоритма сортировки всплывающего пузырька. Реализуйте его для вводимого списка целых чисел.
    Результат выведите в виде списка чисел одну строку через пробел.
    '''
    lst = [4, 5, 2, 0, 6, 3, -56, 3, -1]
    #arr = list(map(int, input().split()))
    for i in range(len(lst)):
        k = i
        for j in range(i, len(lst)):
            if lst[j] < lst[k]:
                k = j
        lst[i], lst[k] = lst[k], lst[i]
    print(*lst)
    return 0
#ex567()

def ex568():
    '''
    В некоторой стране используются денежные купюры достоинством в 1, 2, 4, 8, 16, 32 и 64.
    Вводится натуральное число n. Как наименьшим количеством таких денежных купюр можно выплатить сумму n?
    Вывести на экран список купюр для формирования суммы n (в одну строчку через пробел,
    начиная с наибольшей и заканчивая наименьшей).
    Предполагается, что имеется достаточно большое количество купюр всех достоинств.
    '''
    N = int(input())
    lst_end = []
    lst = [64, 32, 16, 8, 4, 2, 1]
    for i in lst:
        if N // i != 0:
            a = N // i
            lst_end.append([i] * a)
            N = N % i

    for j in lst_end:
        print(*j, end=' ')
    return 0
#ex568()

def Pascal_Triangle():
    N = 100
    P = []
    for i in range(N):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = P[i - 1][j - 1] + P[i - 1][j]
        P.append(row)

    for r in P:
        print(r)
    return 0
#Pascal_Triangle()

#5.8 Генераторы списков (List comprehension)
# Переменная = <Способ формирования значения> for <Переменная> in <Итерируемый объект>
def ex580():
    '''Возведение в степень всех элементов списка'''
    N = 6
    # С использованием цикла for
    a = [0] * N
    for i in range(N):
        a[i] = i ** 2
    print(a)
    # С использованием генератора списков
    b = [x ** 2 for x in range(N)]
    print(b)
    return 0
#ex580()

def ex581():
    '''
    Вводятся вещественные числа в строку через пробел.
    Необходимо на их основе сформировать список lst с помощью list comprehension (генератора списков)
    из модулей введенных чисел (в списке должны храниться именно числа, а не строки).
    Результат вывести на экран в виде списка командой:
    print(lst)
    '''
    inp = list(map(float, input().split()))
    #i = abc
    lst = [abs(d) for d in inp]
    print(lst)
    #abc(d)
    return 0
#ex581()

def ex582():
    '''
    Вводится семизначное целое положительное число. С помощью list comprehension сформировать список lst,
    содержащий цифры этого числа (в списке должны быть записаны числа, а не строки).
    Результат вывести на экран список командой: print(lst)
    '''
    a = input()
    lst = [int(d) for d in a]
    print(lst)
    return 0
#ex582()

def ex583():
    '''
    Вводится натуральное число N. С помощью list comprehension сформировать двумерный список размером N x N,
    состоящий из нулей, а по главной диагонали - единицы.
    (Главная диагональ - это элементы, идущие по диагонали от верхнего левого угла матрицы до ее нижнего правого угла).
    Результат вывести в виде таблицы чисел как показано в примере ниже.
    '''
    a = int(input())
    lst = [[0 if j != i else 1 for j in range(a)] for i in range(a)]
    for k in range(len(lst)):
        print(*lst[k])
    return 0
#ex583()

def ex584():
    '''
     Вводятся названия городов в строку через пробел. Необходимо сформировать список с помощью list comprehension,
     содержащий названия длиной более пяти символов. Результат вывести в строчку через пробел.
    '''
    cities = ['Казань', 'Уфа', 'Москва', 'Челябинск', 'Омск', 'Тур', 'Самара']
    print(len(cities[1]))
    more5 = [item for j, item in enumerate(cities) if len(item) >= 5]
    print(more5)
    return 0
#ex584()

def ex585():
    '''
    Вводится натуральное число n. Необходимо сформировать список с помощью list comprehension,
    состоящий из делителей числа n (включая и само число n). Результат вывести на экран в одну строку через пробел.
    '''
    n = 10 #int(input())
    print(*[int(i) for i in range(1, n + 1) if n % i == 0])
    return 0
#ex585()

def ex586():
    '''
    Вводится натуральное число N. Необходимо сгенерировать вложенный список с помощью list comprehension,
    размером N x N, где первая строка содержала бы все нули, вторая - все единицы,
    третья - все двойки и так до N-й строки. Результат вывести в виде таблицы чисел как показано в примере ниже.
    '''
    n = -4
    mtx = [[i] * n for i in range(n)]
    [print(*mtx[i]) for i in range(len(mtx))]

    # for i in range(n):
    #     mtx.append(0)
    #     for j in range(n - 1):
    #         mtx[i] = [i] * n
    # for i in range(n):
    #     print(mtx[i])
    #print(mtx)
    return 0
#ex586()

def ex587():
    '''
    Вводится список вещественных чисел. С помощью list comprehension сформировать список,
    состоящий из элементов введенного списка, имеющих четные индексы (то есть, выбрать все элементы с четными индексами).
    Результат вывести на экран в одну строку через пробел.
    '''
    fl_lst = [8.5, 11.3, 1.0, -4.5, 11.34, 6.45]
    even = [fl_lst[i] for i in range(len(fl_lst)) if i % 2 == 0]
    print(*even)
    return 0
#ex587()

def ex588():
    '''
    Вводятся два списка целых чисел одинаковой длины каждый с новой строки.
    С помощью list comprehension сформировать третий список,
    состоящий из суммы соответствующих пар чисел введенных списков.
    Результат вывести на экран в одну строку через пробел.
    '''
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]
    print(*[a[i] + b[i] for i in range(len(a))])
    return 0
#ex588()

def ex589():
    '''
    водится список в формате:
    <город 1> <численность населения 1> <город 2> <численность населения 2> ... <город N> <численность населения N>
    Необходимо с помощью list comprehension сформировать список lst, содержащий вложенные списки из пар:
    <город> <численность населения>
    Численность населения - целое число в тыс. человек. Вывести результат на экран в виде списка командой:
    print(lst)
    '''
    peoples = ['Москва', 15000, 'Уфа', 1200, 'Самара', 1090, 'Казань', 1300]
    lst = [[peoples[i-1], int(peoples[i])] for i in range(1, len(peoples), 2)]
    print(lst)

    return 0
#ex589()

#
#Вложенные циклы и вложенные генераторы списков
#
def ex591():
    '''
     Вводится двумерный список в виде таблицы целых чисел (см. пример ниже).
     С помощью list comprehension преобразовать двумерный список в одномерный так,
     чтобы значения элементов шли в обратном порядке.
     Результат отобразить в виде строки из чисел, записанных через пробел.
    :return:
    '''
    lstin = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
    #lst = [[lstin[-y][-x] for x in range(1, len(lstin) + 1)] for y in range(1, len(lstin) + 1)]
    lst = [lstin[x][::-1] for x in range(len(lstin))]
    lst = lst[::-1]
    [print(*lst[i], end=" ") for i in range(len(lst))]
    return 0
#ex591()

def ex592():
    '''
    Вводится список целых чисел в строку через пробел.
    С помощью list comprehension сформировать из них двумерный список lst размером N x N (квадратную таблицу чисел).
    Гарантируется, что из набора введенных чисел можно сформировать квадратную матрицу (таблицу).
    Результат отобразить в виде списка командой:
    print(lst)
    Sample Input:
    1 2 3 4 5 6 7 8 9
    Sample Output:
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    '''
    lst_in = list(map(int, input().split()))
    print(lst_in)
    matrix_size = int(len(lst_in) ** 0.5)
    print(matrix_size)
    lst = [[lst_in[matrix_size * y + x] for x in range(matrix_size)] for y in range(matrix_size)]
    print(lst)
    #lst =
    return 0
#ex592()

def ex593():
    '''
    Используйте следующий список из строк:
    Необходимо преобразовать его в двумерный (вложенный) список lst,
    где каждая строка представляется списком из слов (слова разделяются пробелом),
    но сохранять слова только длиной более трех символов.
    Решить данную задачу с использованием list comprehension. Результат отобразить с помощью команды:
    print(lst)
    Sample Output:
    [['Скажи-ка,', 'дядя,', 'ведь', 'даром'], ['Python', 'выучил', 'каналом'], ['Балакирев', 'раздавал?'], ['Ведь', 'были', 'заданья', 'боевые,'], ['говорят,', 'какие!'], ['Недаром', 'помнит', 'Россия'], ['рубили', 'тогда!']]
    '''
    t = ["– Скажи-ка, дядя, ведь не даром",
         "Я Python выучил с каналом",
         "Балакирев что раздавал?",
         "Ведь были ж заданья боевые,",
         "Да, говорят, еще какие!",
         "Недаром помнит вся Россия",
         "Как мы рубили их тогда!"
         ]
    lst = [t[i].split() for i in range(len(t))]
    lst = [[x for x in lst[y] if len(x) > 3] for y in range(len(lst))]
    print(lst)
    return 0
#ex593()

def ex594():
    '''
    Повторите задачу с транспонированием прямоугольной матрицы с помощью list comprehension,
    изложенной в видео-уроке к этой практике. На вход поступает таблица целых чисел,
    на выходе нужно отобразить эту же таблицу в транспонированном виде (строки заменяются на столбцы),
    используя команду:
    for row in A:
        print(*row)
    где A - транспонированный двумерный список. Желательно сделать эту задачу не пересматривая видео.
    P. S. Для считывания списка целиком в программе уже записаны начальные строчки.
    Sample Input:
    1 2 3
    4 5 6
    7 8 9
    5 4 3
    Sample Output:
    1 4 7 5
    2 5 8 4
    3 6 9 3
    '''
    lst_in = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [5, 4, 3]]
    A = [[a[i] for a in lst_in] for i in range(len(lst_in[0]))]
    for row in A:
        print(*row)
    return 0
#ex594()

#def test():
    # for j in :
    #     for i in range(5):
    #         print(f'{i} in {j}')
    # return 0
#test()