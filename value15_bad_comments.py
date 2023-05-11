Найдите 15 своих плохих комментариев, и напишите по каждому,
что вы сделали для их улучшения с указанием соответствующего пункта из занятия.
"""

# 1
# Задача о сумме двух чисел, выраженных связными списками (№ 2 на литкоде).
# В задаче использовалась дополнительная функция.
# Код в этой функции насыщен комментариями поясняющими ход решения
# Эти комментарии расценены как бормотание и удалены.

def sum_nodes(N1, N2, mind_value=0):
    if N1 is None and N2 is None:                 
        # когда числа кончились, но есть еще цифра "в уме"
        return (ListNode(mind_value), 0)
    elif N1 is None and N2 is not None:
        # одно из чисел кончилось
        return(ListNode((N2.val + mind_value)% 10), (N2.val + mind_value)// 10)
    elif N2 is None and N1 is not None:
        # или другое кончилось
        return(ListNode((N1.val + mind_value)% 10), (N1.val + mind_value)// 10)
    else:
        # есть оба числа и "в уме"
        return(ListNode((N1.val + N2.val + mind_value) % 10),
               (N1.val + N2.val + mind_value) // 10)


# 2
# Задача "Поиск самой длинной подстроки" (№ 3 на Литкоде)
# Код насыщен комментариями поясняющими ход решения
# Эти комментарии  расценены как избыточные и удалены.
def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    k = len(s)
    result = []                             # список с размерами неповторяющих кусочков строки
    while len(s) > 1:                       # цикл повторяется пока не иссякнет строка (более одного символа)
        i = 1
        for current in s[1:]:               # пробегаем по строке, начиная со второго символа
            if current in s[:i]:            # если встретилась повторяющаяся буква
                result.append(len(s[:i]))   # заносим размер кусочка ДО ВТОРОЙ в паре ПОВТОРЯЮЩЕЙСЯ буквы в результаты
                s = s[s.index(current)+1:]  # и удаляем  кусочек до ПЕРВОЙ повторяющейся (ВКЛЮЧИТЕЛЬНО)
                break
            elif i == len(s) - 1:           # если до конца строки повторов не встретилось
                result.append(len(s))       # заносим в ответы длину остатка
                s = s[:i]
            i += 1
    if len(s) == 1:
        result.append(1)
    if len(result) == 0:
        return k
    return max(result)


# 3
# Задача threeSum (№ 15 на Ликоде)
# Код насыщен комментариями поясняющими ход решения
# Эти комментарии расценены как избыточные и удалены.
def threeSum(self, nums):
    res = []
    nums.sort()                     #Sort the array so that we can avoid redundant elements    
    for i, n in enumerate(nums):
        print(i, n)
        if i>0 and n == nums[i - 1]:    #Find first element | avoid repetition
            continue            
        l, r = i+1, len(nums) - 1       #For rest of array, maintain left pointer and right pointer as array is sorted        
        while l<r:
            s = n + nums[l] + nums[r]       #Possible 3sum
            if s > 0:                       #If it is more than 0, then slide the window from right so that sum decreases (Array is sorted)
                r -= 1
            elif s < 0:                     #If it is less than 0, then slide th window from left so that the sum increases.
                l += 1                      
            else:
                res.append([n,nums[l],nums[r]])     #If it is equal to 0, add it to result set
                l += 1                              #Increase left pointer by 1. Note: We need not decrease right window as it will automatically decrease upon condition check of s>0
                while nums[l] == nums[l-1] and l<r:
                    l += 1                  #Slide continuosly till left pointer value is same as previous. Note: Right pointer will correspondingly shift left-ward
    return res

# 4
# Задача  myAtoi( (№ 8 на Литкоде)
# Решение разделено на логические шаги
# Каждый такой "шаг" отделен пустой строкой и описан комментарием
# Я заменил такие блоки кода на функции с "говоряшими" названиями
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
def remove_leading_spaces(text):
    Spases = True
    i = 0
    while Spases and i < len(text):
        if text[i] == ' ':
            i += 1
        else:
            Spases = False
    return text


class Solution:
    def myAtoi(self, s: str) -> int:
        res = []
        if len(s) == 0:
            return 0
        s = remove_leading_spaces(s)
        ...

# 5
# Задача threeSumClosest (№ 16 на Литкоде)
# В коде есть комментарии поясняющие ход решения
# Эти комментарии расценены как избыточные и удалены.
class Solution:
    def threeSumClosest(self, nums, target):

        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans


# 6
# Задача fourSum (№ 18 на Литкоде)
# После основного решения идет блок кода озаглавленный (комментарием)
# "Избавление от повторов"
# Я вынес эти действия в отдельную функцию с понятным названием
# Было
def fourSum(self, nums, target):
    ...
    # избавимся от повторов
    for i in range(len(res) - 1, 0, -1):
        if res[i] in res[:i]:
            res.pop(i)
    ...


# Стало
def remove_repetitions(res):
    for i in range(len(res) - 1, 0, -1):
        if res[i] in res[:i]:
            res.pop(i)
    return res


def fourSum(self, nums, target):
    ...
    res = remove_repetitions(res)
    ...


# 7
# Задача "Перестановки скобок" № 22 на Литкоде
# В коде много комментариев, которые не помогают раскрыть решение,а только отвлекают
# Эти комментарии расценены как бормотание и удалены.

class Solution:
    def generateParenthesis(self, n):
        res = []
        if n == 0:
            return res
        if n == 1:
            return ['()']
        prev = self.generateParenthesis(n - 1)
        for permutation in prev:
            # перебираем предыдущие перестановки
            for position_open in range(len(permutation) + 1):
                # перебираем места для открывающей скобки
                permutation1 = permutation[:position_open] + '(' + permutation[position_open:]
                for position_closed in range(position_open + 1, len(permutation1) + 1):
                    # перебираем мест для закрывающей скобки (только правее открывающей)
                    permutation2 = permutation1[:position_closed] + ')' + permutation1[position_closed:]
                    if not permutation2 in res:
                        # избегаем повторений
                        res.append(permutation2)
        return res

# 8
# Задача longestPalindrome (№ 5 на Литкоде)
# В коде много комментариев которые разъясняют ход решения
# Сами по себе они малоинформативны и не дают дополнительой информации
# Эти комментарии расценены как бормотание и удалены.

class Solution(object):
    def longestPalindrome(self, s):
        ...
        palindroms = []
        # создаем список всех подстрок-палиндромов
        for i in range(len(s) - 1):
            for j in range((i + 1), len(s)):
                if ispalindrom(s[i:j+1]):
                    palindroms.append([len(s[i:j+1]), s[i:j+1]])
        if len(palindroms) == 0:
            return s[0]
        max_len = palindroms[0][0]
        result = palindroms[0][1]
        for i in range(len(palindroms)):                # пробегаем по списку палиндромов
            if palindroms[i][0] > max_len:  # находим максимальное значение длины палиндрома
                max_len = palindroms[i][0]
                result = palindroms[i][1]   # и запоминаем его значение
        return result

# 9
# Задача  Valid Parentheses (№ 20 на Литкоде)
# Комментарий в решении не несет дополнительной информации 
# (код в следующей строке очевиден и достаточно нагляден)
# Комментарий удален
def isValid(self, s):
    Stack_List = []
    Open_Brackets = ['(', '{', '[']
    Close_Brackets = [')', '}', ']']
    for i in range(len(s)):
        if s[i] in Open_Brackets:
             Stack_List.append(s[i])
        else:
            # Проверка что массив не пуст и проверка соответствия скобок
            if len(Stack_List) == 0 or Close_Brackets.index(s[i]) != Open_Brackets.index(Stack_List[-1]):
                return False
            Stack_List.pop()
    return len(Stack_List) == 0

# 10
# Задача mergeTwoLists (№ 21 на Литкоде)
# Решение разделено на логические "шаги", каждый такой шаг предварен комментарием
# Эти комментарии расценены как избыточные и удалены
class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        # Сначала сравниваем головы, чтоб установить указатель head
        ...
        
        # Затем сравниваем  ноды до тех пор, пока какой-нибудь список не закончится
        while current1 is not None and current2 is not None:
            ...
            
# 11
# Задача swapPairs (№ 24 на Литкоде)
# Решение содержит комментарии иллюстрирующие логику размышлений
# Эти комментарии расценены как избыточные и удалены

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: List[ListNode]
        :rtype: ListNode
        """
        # Если на вход подан пустой список или состоящий из елинственной ноды
        if head is None or head.next is None:
            return head
        # Сначала переворачиваем первые два элемента списка (head и head.next)

                            # БЫЛО   A -> B -> C ...
                            #       head
        
        A = head        # первый член
        B = head.next   # второй член
        head = B
        A.next = B.next
        B.next = A

                            # СТАЛО  B -> A -> C ... 
                            #       head

        # переходим к следующей паре
        ...


# 12
# Задача Divide Two Integers (№ 29 на Литкоде)
# Решение содержит комментарии иллюстрирующие логику размышлений
# Эти комментарии расценены как избыточные и удалены

class Solution:
    def divide(self, dividend, divisor):
        positive = dividend >= 0 and divisor >= 0 or dividend < 0 and divisor < 0       # флаг обозначающий знак результата
        if abs(divisor) == 1:
            result = abs(dividend)                        # частный случай - деление на 1
        elif abs(dividend)  < abs(divisor):               # если делимое меньше делителя - вернем 0
            result = 0
        else:
            # сначала избавимся от знаков - будем работать с абсолютными значениями
            divisor = str(abs(divisor))         
            dividend = str(abs(dividend))
            # забронируем  ячейку для результата
            result = ''     
            current = dividend[:len(divisor)]                       # отрезаем первый кусок, равный по длине делителю
            next_sign_index = len(current)                          # индекс следующей цифры 
            if int(current) <int(divisor):
                current += dividend[next_sign_index]
                next_sign_index += 1
            letter, ostatok = division(current, divisor)        # производим  деление первого куска
            result += letter                                    # записываем результат
        
            while next_sign_index < len(dividend):
                current = ostatok + dividend[next_sign_index]       # смещаем кусок
                next_sign_index += 1                                # и смещаем позицию следующей цифры
                letter, ostatok = division(current, divisor)        # производим  деление очередного куска
                result += letter                                    # записываем результат
            result = int(result)
    ...


# 13
# В задаче  Palindrome Number (№ 9 на Литкоде) реализованы два варианта решения.
# При подаче файла на оценку, один из вариантов решения был закомментирован
# Этот закомментированный блок кода удален
class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     left = 0
    #     right = len(s) - 1
    #     while left < right:
    #         if s[left] != s[right]:
    #             return False
    #         left += 1
    #         right -= 1
    #     return True
    
    def isPalindrome(self, x: int) -> bool:
        ...

# 14
# Задача searchInsert (№ 35 на Литкоде)
# В решении много комментариев, которые проясняют ход логических рассуждений.
# Поскольку эта логика реализована в коде, комментарии становятся бессмысленными
# Они расценены как бормотание и удалены

class Solution:
    def searchInsert(self, nums, target):
        # сначала отсечем крайние случае - когда target лежит за пределами списка
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        # далее реализуем рекурсивный двоичный поиск
        right = len(nums) - 1
        return self.search_recursive(nums, target, 0, right)

    def search_recursive(self, nums, target, left, right):
        if left == right:
        # поиск в единичном списке
            if target <= nums[left]:
                return left
            else:
                return right + 1
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid          # если результат найден
        if target < nums[mid] and left == mid:
            # если в рассматриваемом фрагменте 1 или 2 элемента, то mid занимает место левой границы
            return left
            # вставляем вместо левой границы, весь кусок сдвигается вправо на 1   
        if target < nums[mid]:
            # если в рассматриваемом куске  3 или больше элементов - ищем левее mid
            return self.search_recursive(nums, target, left, mid - 1)
        if target > nums[mid]:
            # ищем правее mid
            return self.search_recursive(nums, target, mid+1, right)

# 15
# Задача Find First and Last Position of Element in Sorted Array (№ 34 на литкоде)
# В решении много комментариев, которые проясняют ход логических рассуждений.
# Поскольку эта логика реализована в коде, омментарии становятся бессмысленными
# Они расценены как бормотание и удалены

def binary_search(nums, target, left=0, right=float('inf')):
    if right > len(nums):
        right = len(nums)
    if left == right:
        return -1       # в пустом куске списка target отсутствует
    center = (left + right) // 2
    if nums[center] == target:  # искомый индекс target
        return center
    if target < nums[center]:
        return binary_search(nums, target, left, center)
        # ищем в левой половине куска
    if target > nums[center]:
        return binary_search(nums, target, center + 1, right)
        # ищем в правой половине куска





# В задачах для Литкода для проверки решения я писал юнит-тесты.
# Для упрощения, они хранились в том же файле, что и решение задачи, вызывались вручную
# В момент подачи файла на сервер (для оценки), тесты были закомментированы
# Тесты убраны в другой файл (в который импортируется Solution)
