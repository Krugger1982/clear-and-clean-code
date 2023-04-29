# Сделайте 3 примера с разбором различного времени связывания в вашем коде
# и поясните, почему в каждом случае был сделан такой выбор.

1
# Проект на Django (учебный) - социальная сеть.
# В задании было указано - подключить пагинацию (по 10 постов на страницу)
# По рекомендации ревьюера избавился от "магического числа" 10, упаковав его в константу.
# Файл views.py
from django.core.paginator import Paginator
...
PAGINATION_COUNT = 10
...
def get_page_from_paginator(list_items, request):
    """ Функция для вызова паджинатора.
        Возвращает объект page_obg с разбитыми постранично элементами.
        """
    page_number = request.GET.get('page')
    p = Paginator(list_items, PAGINATION_COUNT)
    page_obj = p.get_page(page_number)
    return page_obj

# Улучшение заключается в осознании той мысли, что пагинация может понадобиться
# и в других приложениях, а при изменении внешнего вида страниц придется везде менять
# значение размера страницы, поэтому константу PAGINATION_COUNT
# целесообразно вынести в настройки проекта

from django.core.paginator import Paginator
from django.conf import settings
...
def get_page_from_paginator(list_items, request):
    """ Функция для вызова паджинатора.
        Возвращает объект page_obg с разбитыми постранично элементами.
        """
    page_number = request.GET.get('page')
    p = Paginator(list_items, settings.PAGINATION_COUNT)
    page_obj = p.get_page(page_number)
    return page_obj
# связыване переменной с объектом теперь происходит при вызове метода get_page_from_paginator
# гибкость кода стала лучше


2
# Учебный проект - телеграм-бот (работает с API Яндекс-практикума,
# шлет в чат результаты проверки задач)
# Для отправки сообщений в чат боту нужен CHAT_ID (номер чата)
# он хранится в переменных окружения, но вызыватся в переменную в начале файла main
# связывание переменной происходит с запуском программы, но при этом боту не требуется
# постоянно лазить в .env-файл за данными.

TELEGRAM_CHAT_ID = os.getenv('CHAT_ID')
...
def send_message(bot, message):
    """Отправляет сообщение 'message' боту 'bot'."""
    try:
        logger.debug(f'Бот отправляет сообщение: {message}')
        bot.send_message(
            chat_id=TELEGRAM_CHAT_ID,
            text=message
        )
    except Exception:
        logger.error('Не удалось отправить сообщение')
        raise exceptions.SendMessageError('Не удалось отправить сообщение')
    else:
        logger.debug('Сообщение успешно отправлено')

3
# в этом же приложении, сам бот инициируется не в момент отправки сообщения, а в начале
# главной рабочей функции main(), то есть создатся один раз за время работы программы
import telegram

TELEGRAM_TOKEN = os.getenv('TOKEN')
RETRY_PERIOD = 600
...
def main():
    """Основная логика работы бота."""
    ...
    bot = telegram.Bot(token=TELEGRAM_TOKEN)
    while True:
        try:
            ...
            # формируется сообщение по результатам запроса к API
            send_message(bot=bot, message=message)
        except Exception as error:
            message = f'Сбой в работе программы: {error}'
            logger.error(message)
        finally:
            time.sleep(RETRY_PERIOD)
# связывание сущности "Бот" с именем переменной bot производится в начале выполнения программы
