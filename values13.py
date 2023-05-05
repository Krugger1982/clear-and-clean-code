"""
3. Задания
3.1. Прокомментируйте 7 мест в своём коде там, где это явно уместно.
"""

1
# Задача о зарплатах (курс 24 задачи)
# добавлен комментарий объясняющий блок кода


def SynchronizingTables(N, ids, salary):
    ids2 = []
    for i in range(N):
        ids2.append(ids[i])         
    ids2 = sorted(ids2)
    salary = sorted(salary)
    salary2 = []
    # Сопоставляем элемент двух упорядоченных списков
    for i in range(N):                 
        for j in range(N):             
            if ids[i] == ids2[j]:       
                salary2.append(salary[j])    
    return salary2

2
# Задача о взломе мобильных


def PatternUnlock(N, hits):
    ...
    # Избавляемся от нулей в полученном числе
...
# добавлен комментарий объясняющий блок кода

3
# Задача о разности длинных чисел (курс 24 задачи)
# добавлен комментарий объясняющий блок кода
def BigMinus(s1,s2):
    S1 = list(s1)
    S2 = list(s2)
    bol = [0]
    men = [0]
    # Так как для вычитания положение элементов имеет значение,
    # расставляем числа в правильном порядке, большее - в начале
    # для чисел равной длины проведем поразрядное сравнивание
    if len(S1) > len(S2):
        bol = S1
        men = S2
    elif len(S2) > len(S1):
        bol = S2
        men = S1
    else:
        for i in range(len(S1)):
            if S1[i] > S2[i]:
                bol = S1
                men = S2
                break
            elif S1[i] < S2[i]:
                bol = S2
                men = S1
                break
        ...
4
# Задача о выборах (курс 24 задачи)
# добавлен комментарий объясняющий блок кода

def MassVote(N, Votes):
    Copy = sorted(Votes, reverse=True)
    # Если лидеров больше одного с равными результатами
    if N != 1 and Copy[1] == Copy[0]:
        return 'no winner'
    ...

5
# Задача о бухгалтере Оксана (курс 24 задачи)
# Добавлен докстринг, объясняющий неочевидную логику решения

def SumOfThe(N, data):
    """ так как список data содержит несколько чисел и вдобавок их сумму S, 
    то посчитав сумму элементов data получим удвоенную сумму S.
    """
    return sum(data)/2


6
# Задача о расшифровке кодов НЛО (курс 24 задачи)
# Добавлен докстринг, объясняющий неочевидную логику решенияdef UFO(N, data, octal):

def UFO(N, data, octal):
    """ Перевод числа из любой системы в десятичную можно представить как некую сумму.
        произведений основания системы счисления на значение разряда.
        Очевидно, что во входных данных не будет букв,
        характерных для шестнадцатеричной системы (A=10, B=11, C=12 и т.д.)
        и не требуется писать для них расшифровку. 
        Тогда можно свести всю программу к простому суммированию числового ряда.
    """
    if octal:
        X = 8
    else:
        X = 16
    for i in range(N):
        S = list(str(data[i]))
        Number = 0
        S.reverse()
        for j in range(len(S)):
            Number += int(S[j]) * (X**j)
        data[i] = Number
    return data

7
# Задача о Яндекс-такси (курс 24 задачи)
# добавлен комментарий объясняющий блок кода


def Unmanned(L, N, track):
    ...
    # на каждой итерации пробегаем по светофорам
    # и определяем его flag (красный или зеленый)
    while S < L:
        for j in range(N):
            track[j][3] = not ((t % (track[j][1] + track[j][2])) < track[j][1])
            if S == track[j][0]:
                Step = Step and track[j][3]
        if Step:
            S += 1
        t += 1
    return t



"""
3.2. Если вы раньше делали комментарии к коду, найдите 5 мест,
где эти комментарии были излишни, удалите их и сделайте сам код более наглядным.
"""
1
# Задача о разности длинных чисел (курс 24 задачи)
# После добавления комментария видно, что вместо поясняющего комментария,
# лучше вынести этот блок в отдельную функцию и дать ей говорящее название
def sort_numbers(S1, S2):
    S1 = list(s1)
    S2 = list(s2)
    bol = [0]
    men = [0]
    if len (S1) > len (S2):
        bol = S1
        men = S2
    elif len (S2) > len (S1):
        bol = S2
        men = S1
    else:
        for i in range(len(S1)):
            if S1[i] > S2[i]:
                bol = S1
                men = S2
                break
            elif S1[i] < S2[i]:
                bol = S2
                men = S1
                break
    return bol, men

def BigMinus(s1,s2):
    S1, S2 = sort_numbers(S1, S2)
    ...

2
# Задача о выборах (курс 24 задачи)
# Вместо поясняющего комментария,
# лучше вынести этот блок в отдельную функцию и дать ей говорящее название
def is_equal_votes(N, Votes):
    return N != 1 and Votes[1] == Votes[0] 
def MassVote(N, Votes):
    if is_equal_votes(N, Votes):
        return 'no winner'
    ...
    
3
# Задача о вращении матрицы (курс 24 задачи)
# Блок кода с "разборкой" матрицы на "периметры" объясняется комментарием
# лучше вынести этот блок в отдельную функцию и дать ей говорящее название
def perimetres(A, N, M):
    perimetr = []
    temp = []
    while len(A) > 2 and len (A[0]) > 2:
        for i in range(len(A[0])):
            temp.append(A[0][i])
        del A[0]
        for i in range(len(A)-1):
            temp.append(A[i][len(A[i])-1])
            del A[i][len(A[i])-1]
        for i in range(-1, -len(A[len(A)-1])-1, -1):
            temp.append(A[len(A)-1][i])
        del A[len(A)-1]
        for i in range(-1, -len(A)-1, -1):
            temp.append(A[i][0])
            del A[i][0]
        perimetr.append(temp)
        temp = []
    if N >= M:
        for i in range(len(A[0])):
            temp.append(A[0][i])
        del A[0]
        for i in range(-1, -len(A[0])-1, -1):
            temp.append(A[0][i])
        del A[0]
    else:
        temp.append(A[0][0])
        for i in range(len(A)):
            temp.append(A[i][1])
            del A[i][1]
        for i in range(-1, -len(A), -1):
            temp.append(A[i][0])
        del A
    perimetr.append(temp)
    perimetr.reverse()

4
# В задаче MergeTwoLists (№ 21 Leetcode) выбор "головы" итогоого списка можно 
# отделить  в отдельную функцию
# Было
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # Сначала сравниваем головы, чтоб установить указатель head
        current1 = l1
        current2 = l2
        if current1.val <= current2.val:
            head = l1
        else:
            head = l2
        ...
3 # Стало
def get_head(list1, list2):
    current1 = list1
    current2 = list2
    if current1.val <= current2.val:
        head = list1
    else:
        head = list2
    return head


class Solution:
    def mergeTwoLists(self, l1, l2):
        ...
        head = get_head(l1, l2)
        ...
5
# Задача myAtoi (№ 8 на leetcode)
# Блок кода, отмеченный комментарием "убираем нули"
# можно вынести в отдельную функцию и дать ей  наглядное имя
# Было
class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        if len(s) == 0:
            return 0
        
        # Убираем ведущие пробелы
        Spases = True
        i = 0
        while Spases and i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                Spases = False
        ...

# Стало
def delete_spases(s):
    Spases = True
    i = 0
    while Spases and i < len(s):
        if s[i] == ' ':
            i += 1
        else:
            Spases = False
    return i


class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        if len(s) == 0:
            return 0
        
        # Убираем ведущие пробелы
        Spases = True
        i = 0
        while Spases and i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                Spases = False
