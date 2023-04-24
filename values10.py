# Внесите 15 правок в свой код с учётом рекомендаций из данного занятия,
# и напишите по каждой, как и что конкретно вы улучшили.


1
#   Задача "редактор Лапоть" (24 задачи)
# Было:
position = [['', 1]]
N = 0

def BastShoe(command):
    global position
    global N
    ...


#  Вместо глобальных переменных я ввел класс состояний редактируемой строки.
# Стало:
class Position():
    def __init__(self) -> None:
        self.position = []

    def undo(self, current_position):
        ...

    def redo(self, current_position):
        ...


2
#   Задача "Добавление двух чисел" Литкод, № 2
# Было:
class Solution():
    def addTwoNumbers(l1, l2):
        ...
        Res = ListNode()
        current = _Res
        ...

#  Переменную Res я сделал приватной (только внутри класса).
# Стало:

class Solution():
    def addTwoNumbers(l1, l2):
        ...
        __Res = ListNode()
        current = __Res
        ...

3
#   Задача "Длина самой длинной подстроки" Литкод, № 3
# Было:
class Solution():
    def lengthOfLongestSubstring(s):
        ...
        k = len(s)
        result = []
        ...

#  Переменные k и result я сделал приватной (используются только внутри класса).
# Стало:
class Solution():
    def lengthOfLongestSubstring(s):
        ...
        __k = len(s)
        __result = []
        ...


4
#   Задача " Самый длинный палиндром-подстрока" Литкод, № 5
# Было:
class Solution():
    def longestPalindrome(self, s):
        ...
        palindroms = []
        ...

#  Переменную palindroms я сделал приватной (используется только внутри класса).
# Стало:
class Solution():
    def longestPalindrome(self, s):
        ...
        __palindroms = []
        ...


5
#   Задача " Zigzag Conversion" Литкод, № 6
# Было:
class Solution():
    def convert(self, s, numRows):
        ...
        matrix = []
        ...

#  Переменную matrix я сделал приватной (используется только внутри класса).
# Стало:
class Solution():
    def convert(self, s, numRows):
        ...
        __matrix = []
        ...


6 

#   Задача "Reverse Integer" Литкод, № 7
# Было:
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            res = int(str(x)[::-1])
        else:
            res = - int(str(- x)[::-1])
        if res > 2 ** 31 - 1  or res < - 2 ** 31:
            return 0
        return res

#  Переменную res я сделал приватной (используется только внутри класса).
# Стало:
class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            __res = int(str(x)[::-1])
        else:
            __res = - int(str(- x)[::-1])
        if __res > 2 ** 31 - 1  or __res < - 2 ** 31:
            return 0
        return __res


7
#    Задача "Palindrome Number" Литкод, № 9
# Было:  
class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        ...
#  Переменную s я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        __s = str(x)
        ...


8
#    Задача о бассейне "Container With Most Water" Литкод, № 11
# Было:  
class Solution:
    def maxArea(self, height):
        volume = -1
        ...
        return volume
        ...
#  Переменную volume я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def maxArea(self, height):
        __volume = -1
        ...
        return volume
        ...



9
# Задача  "Integer to Roman" Литкод, № 12
# Было:  
class Solution:
    def intToRoman(self, num):
        Romans = [...]
        ...
#  Переменную Romans я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def intToRoman(self, num):
        __Romans = [...]
        ...


10
# Задача  "Roman to Integer" Литкод, № 13
# Было:  
class Solution:
    def romanToInt(self, s: str) -> int:
        Letters = {...}
        ...
#  Переменную Letters я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def romanToInt(self, s: str) -> int:
        __letters = {...}
        ...

11
# Задача  "Longest Common Prefix" Литкод, № 14
# Было:  
class Solution:
    def longestCommonPrefix(self, strs):
        ...
        res = ''
        ...
#  Переменную res я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def longestCommonPrefix(self, strs):
        ...
        __res = ''
        ...


12
# Задача  "3Sum" Литкод, № 15
# Было:  
class Solution:
    def threeSum(self, nums):
        ...
        res = []
        ...
#  Переменную res я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def threeSum(self, nums):
        ...
        __res = []
        ...


13
# Задача  "3Sum Closest" Литкод, № 16
# Было:  
class Solution:
    def threeSumClosest(self, nums, target):
        ...
        ans = nums[0] + nums[1] + nums[2]
        ...
#  Переменную ans я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def threeSumClosest(self, nums, target):
        ...
        __ans = nums[0] + nums[1] + nums[2]
        ...
 

14
# Задача  "Letter Combinations of a Phone Number" Литкод, № 17
# Было:  
class Solution:
    def letterCombinations(self, digits):
        result = []
        ...
#  Переменную result я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def letterCombinations(self, digits):
        __result = []
        ...  

15
# Задача  "4Sum Combinations of a Phone Number" Литкод, № 18
# Было:  
class Solution:
    def fourSum(self, nums, target):
        res = []
        ...
#  Переменную res я сделал приватной (используется только внутри класса).
# Стало:        
class Solution:
    def fourSum(self, nums, target):
        __res = []
        ...   
