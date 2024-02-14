# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Album:
    def __init__(self, band: str, name: str, songs_quantity: int, songs_number: int):
        """
        Создание и подготовка к работе объекта "Альбом"
        :param band: Название группы
        :param name: Название альбома
        :param songs_quantity: Количество песен в альбоме
        :param songs_number: Номер прослушиваемой песни
         Примеры:
        >>> glass = Album('Linkin Park', 'Minutes to midnight,', 14, 1)  # инициализация экземпляра класса
        """
        if not isinstance(band, str):
            raise TypeError('Название группы должно быть типа str')
        self.band = band
        if not isinstance(name, str):
            raise TypeError('Название альбома должно быть типа str')
        self.name = name
        if not isinstance(songs_number, int):
            raise TypeError('Количество прослушанных песен должно быть типа int')
        if not isinstance(songs_quantity, int):
            raise TypeError('Количество песен в альбоме должно быть типа int')
        if not songs_number > 0 or not songs_quantity > 0 or not songs_number <= songs_quantity:
            raise ValueError('Количество песен должно быть больше 0 и количество прослушанных песен'
                             ' не может быть больше количества песен в альбоме')
        self.songs_quantity = songs_quantity
        self.songs_number = songs_number

    def actual_song(self, listened_songs: int):
        """
        Функция увеличивает прослушиваемую песню
        :return: Актуальная прослушиваемая песню
        :param listened_songs: Прослушано песен
        Примеры:
        >>> glass = Album('Linkin Park', 'Minutes to midnight,', 14, 1)
        >>> glass.actual_song(5)
        """
        if not isinstance(listened_songs, int):
            raise TypeError('Количество прослушанных песен должно быть типа int')

    def listened_album(self) -> bool:
        """
        Функция проверяет прослушан ли альбом
        :return: Проверяет прослушан ли альбом
        Примеры:
        >>> glass = Album('Linkin Park', 'Minutes to midnight,', 14, 1)
        >>> glass.listened_album()
        """


class Door:
    def __init__(self, height: int, width: int, opened_door: bool):
        """
        Создание и подготовка к работе объекта "Дверь"
        :param height: Высота двери
        :param width: Ширина двери
        :param opened_door: Открыта ли дверь
         Примеры:
        >>> glass = Door(2100, 1200, False)  # инициализация экземпляра класса
        """
        if not isinstance(height, int):
            raise TypeError('Высота двери должна быть типа int')
        self.height = height
        if not isinstance(width, int):
            raise TypeError('Ширина двери должна быть типа int')
        self.width = width
        if not isinstance(opened_door, bool):
            raise TypeError('Ширина двери должна быть типа int')
        self.opened_door = opened_door

    def door_area(self):
        """
        Функция считает площадь дверного проема
        :return: Площадь дверного проема
        Примеры:
        >>> door = Door(2100, 1200, False)
        >>> door.door_area()
        """

    def close_door(self) -> bool:
        """
        Функция закрывает дверь
        :return: Закрытая дверь
        Примеры:
        >>> door = Door(2100, 1200, False)
        >>> door.close_door()
        """

    def open_door(self) -> bool:
        """
        Функция открывает дверь
        :return: Открытая дверь
        Примеры:
        >>> door = Door(2100, 1200, False)
        >>> door.open_door()
        """


class Weathervanes:
    def __init__(self, base_angle: int, rotate_angle: int):
        """
        Создание и подготовка к работе объекта "Флюгер"
        :param base_angle: Исходный угол поворота флюгера
        :param rotate_angle: Угол, на который повернулся флюгер
        """
        if not isinstance(base_angle, int):
            raise TypeError('Исходный угол поворота флюгера должен быть типа int')
        if not isinstance(rotate_angle, int):
            raise TypeError('Угол поворота флюгера должен быть типа int')
        if not base_angle > 0 or not base_angle <= 360:
            raise ValueError('Исходный угол поворота флюгера дожен принадлежать отрезку [0;360]')
        self.base_angle = base_angle
        if not base_angle > -360 or not base_angle <= 360:
            raise ValueError('Угол поворота флюгера дожен принадлежать отрезку [-360;360]')
        self.rotate_angle = rotate_angle

    def meteorological_direction(self) -> int:
        """
        Функция определяет метеорологическое направление ветра
        :return:  Азимут точки, откуда дует ветер
        Примеры:
        >>> wind_1 = Weathervanes(25, 40)
        >>> wind_1.meteorological_direction()
        """

    def aeronautical_direction(self) -> int:
        """
        Функция определяет аэронавигационное направление ветра
        :return:  Азимут точки, куда дует ветер
        >>> wind_1 = Weathervanes(25, 40)
        >>> wind_1.aeronautical_direction()
        """


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass