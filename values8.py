# 1
# Задача о зарплатах (курс 24 задачи)
# Было:
def SynchronizingTables(N, ids, salary):
    ...

# Стало:
from typing import List
def SynchronizingTables(N: int, ids: List[int], salary: List[int]) -> List[int]:
    ...


# 2
# Задача "Разблокировка мобильных телефонов" (курс 24 задачи)
# Было:
def PatternUnlock(N, hits):
    ...

# Стало:
from typing import List
def PatternUnlock(N: int, hits: List[int]) -> str:
    ...


# 3
# Задача "Миссия невыполнима: Красный портфель" (курс 24 задачи)
# Было:
def TheRabbitsFoot(s, encode):
    ...

# Стало:
def TheRabbitsFoot(s: str, encode: bool) -> str:
    ...


# 4
# Задача "Райнехарт и мистер Андерсон" (Разность длинных чисел) (курс 24 задачи)
# Было:
def BigMinus(s1, s2):
    ...

# Стало:
def BigMinus(s1: str, s2: str) -> str:
    ...

# 5
# Задача "146%" (курс 24 задачи)
# Было:
def MassVote(N, Votes):
    ...

# Стало:
from typing import List
def MassVote(N: int, Votes: List[int]) -> str:
    ...

# 6
# Задача "Освобождение квадратов" (курс 24 задачи)
# Было:
def ConquestCampaign(N, M, L, batalion):
    ...

# Стало:
from typing import List
def ConquestCampaign(N: int, M: int, L: int, batalion: List[int]) -> int:
    ...


# 7
# Задача "Поиск слова в тексте" (курс 24 задачи)
# Было:
def WordSearch(Len, s, subs):
    ...

# Стало:
from typing import List
def WordSearch(Len: int, s: str, subs:str) -> List[int]:
    ...


# 8
# Задача "Экономия тонера" (курс 24 задачи)
# Было:
def PrintingCosts(Line):
    ...

# Стало:
def PrintingCosts(Line: str) -> int:
    ...


# 9
# Задача "Искусственный интеллект для Оксаны" (курс 24 задачи)
# Было:
def SumOfThe(N, data):
    ...

# Стало:
from typing import List
def SumOfThe(N: int, data: List[int]) -> int:
    ...

# 10
# Задача "Оптимизация беспилотного трафика" (курс 24 задачи)
# Было:
def Unmanned(L, N, track):
    ...

# Стало:
from typing import List

def Unmanned(L: int, N:int, track:List[List[int]]) -> int:
    ...

# 11
# Задача "Шопоголики" (курс 24 задачи)
# Было:
def MaximumDiscount(N, price):
    ...

# Стало:
def MaximumDiscount(N: int, price: List[int]) -> int:
    ...

# 12
# Задача "" (курс 24 задачи)
# Было:
def BiggerGreater(input):
    ...
    
# Стало:
def BiggerGreater(input: str) -> str:
    ...
