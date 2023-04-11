# 3.1. Сделайте в своём коде три примера наглядных методов-фабрик.

1
# Задача на Яндекс-контесте 
# Реализация dequeue на кольцевой очереди
# На вход поступает название метода и (опционально) - параметр (например, "push_front 10")
# некоторые методы не предполагают параметра 

class Deque:
    def __init__(self, n):
        self.__deque = [None] * n
        self.__max_n = n
        self.__head = 0
        self.__tail = 0
        self.__size = 0
    
    # В этом случае фабрика - это определение метода, который нужно вызвать    
    def call_method(self, name, arg=None):
        if arg is not None:
            return getattr(self, name)(arg)
        return getattr(self, name)()

    def push_back(self, value):
        ...

    def push_front(self, value):
        ...

    def pop_front(self):
        ...

    def pop_back(self):
        ...


2
#  Задача на яндекс-контесте.
# Похожая на предыдущий пример реализация стека


def call_method(obj, name, arg=None):
    if arg is not None:
        return getattr(obj, name)(arg)
    return getattr(obj, name)()


class Stack:
    def __init__(self):
        self.items = []

    def call_method(self, name, arg=None):
        if arg is not None:
            return getattr(self, name)(arg)
        return getattr(self, name)()
    
    def push(self, item):
        ...

    def pop(self):
        ...

    def get_max(self):
        ...

3
# Пример из интернета (из обучающей статьи)
 
class SongSerializer:
    """ Класс позволяет сериализовать данные о музыкальном произведении
        в json или в xml-фомат.
    """
    def serialize(self, song, format):
        serializer = self._get_serializer(format)
        return serializer(song)
    
    def _get_serializer(self, format):
        """ выбор вида сериалайзера - фабричный метод """
        if format == 'JSON':
            return self._serialize_to_json
        elif format == 'XML':
            return self._serialize_to_xml
        else:
            raise ValueError(format)
        
    def _serialize_to_json(self, song):
        payload = {
            'id': song.song_id,
            'title': song.title,
            'artist': song.artist
        }
        return json.dumps(payload)
    def _serialize_to_xml(self, song):
        song_element = et.Element('song', attrib={'id': song.song_id})
        title = et.SubElement(song_element, 'title')
        title.text = song.title
        artist = et.SubElement(song_element, 'artist')
        artist.text = song.artist
        return et.tostring(song_element, encoding='unicode')


# 3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы,
# напишите несколько примеров их правильного именования.
# Для приведенных примеров имена методов-фабрик могут быть изменены 
1, 2
# Было:
def call_method(self, format):
    ...
# Стало:
def method_facrtory(self, format):
    ...


3
# Было:
def _get_serializer(self, format):
    ...
# Стало:
def serializer_factory(self, format):
    ...
