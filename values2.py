6.1.
# Разберите свой код, и сделайте пять примеров,
# где можно более наглядно учесть в именах переменных уровни абстракции.

1.
# Задача "палиндром" из курса "Алгоритмы и структуры данных № 1" (тесты)
# Было:
Ex = 'А Роза упала на лапу Азора'
# Стало:
example_string = 'А Роза упала на лапу Азора'

2.
# Задача "Взлом мобильных телефонов" из курса "24 задачи"
# Было:
step = (hits[i], hits[i+1])
# Стало:
possible_movement = (hits[i], hits[i+1])

3.
# Задача "Бухгалтер Оксана" из курса "24 задачи"
# Было:
S = 0           # Начальное значение суммы чисел в массиве
# Стало:
sum_of_numbers = 0

4. 
# Задача "Яндекс-такси" из курса "24 задачи"
# Было:
Step = True           # флаг обозначает возможность двигаться дальше
# Стало:
movement_possibility = True

5.
# Задача "Гарри Поттер" из курса "24 задачи"
# Было:
S = list(input)           # вводимый текст заклинания
# Стало:
spell_text = list(input) 


6.2
# Приведите четыре примера, где вы в качестве имён переменных
# использовали или могли бы использовать технические термины из информатики.

1.
# Задача- Шопоголичка из курса "24 задачи""
# Было:
Copy = sorted(price, reverse=True)
# Стало:
sorted_list = sorted(price, reverse=True)

2.
# Задача- "Кроличья лапка" из курса "24 задачи""
# Было:
matrix_T = []       # Creating a transposed matrix 
# Стало:
transposed_matrix = []                                

3.
# Задача "Шифрование сигналов НЛО" из курса "24 задачи"
# Было:
X = 8           # Определяем систему счисления
# Стало:
numeral_system = 8

4.
# Задача "Машинное распознавание паттернов" из курса "24 задачи"
# Было:
pat = ''.join(pattern)     # собираем шаблон обратно в строку
# Стало:
templated_string = ''.join(pattern)


6.3
# Придумайте или найдите в своём коде три примера,
# когда имена переменных даны с учётом контекста (функции, метода, класса).

1.
# Задача "Шифрование сигналов НЛО" из курса "24 задачи"
# Было:
Number = 0      # очередная цифра дешифрованного восьмеричного или 16-ричного числа
# Стало:
current_digit = 0

2.
# Задача- "Футбольная команда" из курса "24 задачи""
# Было:
B = []      # Список цепочек несовпадений
# Стало:
differences = []

3.
# Задача- "Шерлок Холмс и его пароли" из курса "24 задачи"
# Было:
S = list(s)     #  преобразование пароля в список символов
# Стало:
letters = list(s)


6.4
# Найдите пять имён переменных в своём коде,
# длины которых не укладываются в 8-20 символов,
# и исправьте, чтобы они укладывались в данный диапазон.

1.
# Задача "Чубакка"из курса "24 задачи"
# Было:
B = Transform(A, N)
# Стало:
trans_array = Transform(A, N)

2.
# Задача "Чубакка"из курса "24 задачи"
# Было:
C = Transform(B, N)
# Стало:
double_trans_array = Transform(trans_array, N)


3.
# Задача "Скобки"
# Было:
def Balanced_Parentheses(N): # длинное имя функции
    ...
# Стало:
def Valid_brackets(N):
    ...

4.
# Задача о захвате Государства Квадратов
# Было:
D = 1       # порядковый номер очередного дня
# Стало:
day_of_operation = 1

5.
# Задача о захвате Государства Квадратов
# Было:
C = 0       # наличие незахваченных территорий
# Стало:
free_territories = 0    
