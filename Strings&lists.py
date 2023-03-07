import math

def stings_addition():
    s1 = (1 + 2) * ('7' + '8')
    s2, s3 = map(str, input("INPUT:").split())
    print(s2, s3)
    return()
#stings_addition()

def str_print():
    s1 = str(input("Введите строку: "))
    print(f"Строка: {s1}. Длина: {len(s1)}")
    return()
#str_print()

def str_index():
    s = 'I love Python'
    print(s[0] + s[-1])
    return()
#str_index()

def str_methods():
    str = "Hello EVERYbody, who perent HERE ToDay!!!"
    str2 = "abrakadabra"
    digits_string = "1951"
    multistring = '''This is
multistring here
right NOW!!!
The enD\n'''
    print(multistring.upper())
    print(str.upper() + "\n") #Метод '.upper' выводит всю строку заглавными буквамию
    print(str.lower()) #Метод '.lower' выводит всю строку прописнымию
    print(str2.count("ra")) #Метод '.count' определяет кол-во указанных повторений
    print(str.find("Da")) #'.find' находит индекс в строке по направлению чтения (rfind ищет в обратном направлении)ю
    print(str.index("EVE")) #Метод '.index', работает также, как find, но выдает ошибку при несуществующем значении.
    print(str.replace("EVERY", "some")) #Метод '.replace' заменяет найденое значение в строке.
    print(str2.isalpha()) #'.isalpha' возвращает 'True', если вся строка состоит из букв (в противном случае - 'False').
    print(str.isdigit()) #противоположен '.isalpha'.
    print(digits_string.rjust(8, "0")) #Заполняет строку до нужного кол-ва символов слево, ljust - справа.
    print(multistring.upper().split(" "))#Метод '.split' разпивает строку на фрагметы по указанному разделителю.
    new_str = multistring.replace("\n", " ").split(" ")
    print(" ".join(new_str))#Метод .join объединяет в единую строку все указанные подстроки.
    print("      HELLO WORLD!      \n".strip())#Удаляет все незначащие символы.
    print("HELLO".lower().replace("h", "H"))
    return()
#str_methods()

def les7():
    str = "dobavlyaem---slagi--slug-k--url---adresam"
    str_rep = str.replace("---", "-").replace("--", "-")
    print(str_rep)
    s1, s2, s3 = input("введите цифры через пробел: ").split()
    print(f'{s1.rjust(3, "0")}\n{s2.rjust(3, "0")}\n{s3.rjust(3, "0")}\n')

    return()
#les7()

def str_format():
    msg = "This {0} string {1}".format("is", "!!!")
    print(msg)
    return 0
#str_format()

def RUB_in_USD():
    rub = 1000
    usd = 73.54
    print(f'Вы можете получить {int(rub / usd)}$ за {rub} рублей по курсу {usd}')
    return 0
RUB_in_USD()

def lists():
    #str = map(int, input().split())
    #lst = list(str)
    #print(lst)
    return 0

def ch_book():
    book_name = str(input())
    writer = str(input())
    num_of_pages = int(input())
    price = float(input())
    book = [book_name, writer, num_of_pages, price]
    book[1] = "Пушкин"
    del book[2]
    book[-1] *= 2
    print(book)
    return 0
#lists()

def lsts2():
    str1 = map(int, input().split(" "))
    lst1 = list(str1)
    print(max(lst1), min(lst1), sum(lst1))
    return 0
#lsts2()

def lsts3():
    str = list(map(int, input().split(" ")))
    lst = sorted(str, reverse=True)
    print(*lst)
    return 0
#lsts3()

def lsts4():
    lst = [1, 2, 7, 8, 4, 3, 79, 154, 2, 3, 67, 0]
    print(lst[::-1]) #Вывод списка в обратном порядке.
    print(lst[4:9:]) #Вывод списка от 4 по 8 индекс(конечный указанный индекс не выводится).
    print(lst[::2]) #Вывод списка с шагом 2.
    print(lst >= [100, 200, 300]) #Сравнение списков.
    return 0
lsts4()

def lst_methods():
    lst = [90, 60, 90]
    print(f'Standard list: {lst}')
    lst.append(1000) #Добавляет эл-т в конец списка
    print(lst)
    lst.insert(1, 666) #Добваляет эл-т в указанное место списка
    print(lst)
    lst.remove(90) #Удаляет эл-т по значению
    print(lst)
    lst.pop(3) #Удаляет эл-т по индексу
    print(lst)
    newlst = lst.copy() #Делает копию списка
    lst.clear() #Очищает список
    print(f'Очищенный список: {lst}')
    print(f'Новая копия списка \'newlst\': {newlst}')
    print(f'Число эл-тов со значением \'666\': {newlst.count(666)}')
    print(f'Index 666 = {newlst.index(666)}')
    newlst.reverse()
    print(newlst)
    newlst.sort()
    print(*newlst)
    return 0
#lst_methods()

def num_change():
    num = list(str(input("Введите номер телефона: ")))
    num.pop(0)
    num.insert(0, 8)
    num.remove('7')
    num.remove('-')
    num.remove('-')
    str_lst = [str(x) for x in num]
    print("".join(str_lst))
    return 0
#num_change()
def num_sort():
    s = input().split()
    s = list(map(int, s))
    s.sort()
    print(s)
    return 0
#num_sort()

def num_bool():
    lst = input().split()
    lst = list(map(int, lst))
    chs = lst[-1] % 2 == 1
    lst.pop()
    lst.append(chs)
    print(*lst)
    return 0
#num_bool()