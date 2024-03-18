import doctest
import datetime


class Artist:
    """ Базовый класс музыкального испольнителя. """

    def __init__(self, name: str, year: int, album_count: int, l_count: int):
        """
        Создание и подготовка к работе объекта "Музыкальный исполнитель"
        :param name: Имя музыкального исполнителя, которое не изменяется
        :param year: Год создания, который не изменяется
        :param album_count: Количество вышедших альбомов
        :param l_count: Общее количество прослушиваний в месяц в приложении Spotify
        Примеры:
        >>> artist = Artist('Muse', 1994, 9, 14256989)
        """
        self._name = name
        self._year = year
        self.album_count = album_count
        self.l_count = l_count

    @property
    def album_count(self) -> int:
        return self._album_count

    @album_count.setter
    def album_count(self, new_album_count: int) -> None:
        if not isinstance(new_album_count, int):
            raise TypeError("Количество альбомов должно быть типа int")
        if not new_album_count > 0:
            raise ValueError("Количество альбомов должно быть больше 0")
        self._album_count = new_album_count

    def total_cost(self) -> float:
        """
        Фукнция определяет заработок от прослушиваний на основе средней цены прослушивания
        :return: Заработок от прослушиваний в месяц в долларах
        """
        return self.l_count * 0.005

    def year_per_album(self) -> int:
        """
        Функция определяет сколько лет требуется на написание альбома
        :return: Количество лет
        """
        current_date = datetime.datetime.now().year
        return (current_date - self._year) // self._album_count

    def __str__(self):
        return f"Исполнитель: {self._name}\nГод создания: {self._year}\nКоличетсво альбомов: {self._album_count}\n" \
               f"Количетсво прослушиваний в месяц: {self.l_count}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, year={self._year!r})," \
               f"album_count={self._album_count!r}, l_count={self.l_count!r}"


class Rock(Artist):
    def __init__(self, name: str, year: int, album_count: int, l_count: int, genre: str):
        """
        Создание и подготовка к работе объекта "Рок-исполнитель"
        :param genre: Жанр рок-музыки
        Примеры:
        >>> artist = Rock('Muse', 1994, 9, 14256989, 'Alternative Rock')
        """
        super().__init__(name, year, album_count, l_count)
        self.genre = genre

    @property
    def genre(self) -> str:
        return self._genre

    @genre.setter
    def genre(self, new_genre: str) -> None:
        if not isinstance(new_genre, str):
            raise TypeError("Жанр альбома должен быть типа str")
        self._genre = new_genre

    def total_cost(self) -> float:
        """
        Фукнция определяет заработок от прослушиваний на основе цены прослушивания в AppleMusic
        :return: Заработок от прослушиваний в месяц в долларах
        """
        return self.l_count * 0.005

    def year_per_album(self) -> int:
        """
        Функция определяет сколько лет требуется на написание альбома
        :return: Количество лет
        """
        return super().year_per_album()

    def __str__(self):
        return f"Исполнитель: {self._name}\nГод создания: {self._year}\nКоличетсво альбомов: {self._album_count}\n" \
               f"Количетсво прослушиваний в месяц: {self.l_count}\nЖанр рок-музыки: {self._genre}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, year={self._year!r})," \
               f"album_count={self._album_count!r}, l_count={self.l_count!r}, genre={self._genre}"


class Rap(Artist):
    def __init__(self, name: str, year: int, album_count: int, l_count: int, alive: bool):
        """
        Создание и подготовка к работе объекта "Рок-исполнитель"
        :param alive: Жив ли артист
        Примеры:
        >>> artist = Rap('эхопрокуренныъподъездов', 2010, 6, 5858, False)
        """
        super().__init__(name, year, album_count, l_count)
        self._alive = alive

    def total_cost(self) -> float:
        """
        Фукнция определяет заработок от прослушиваний на основе цены прослушивания в Spotify
        :return: Заработок от прослушиваний в месяц в долларах
        """
        return self.l_count * 0.0033

    def year_per_album(self) -> int:
        """
        Функция определяет сколько лет требуется на написание альбома
        :return: Количество лет
        """
        return super().year_per_album()

    def __str__(self):
        return f"Исполнитель: {self._name}\nГод создания: {self._year}\nКоличетсво альбомов: {self._album_count}\n" \
               f"Количетсво прослушиваний в месяц: {self.l_count}\nЖив ли артист: {self._alive}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, year={self._year!r})" \
               f"album_count={self._album_count!r}, l_count={self.l_count!r}, alive={self._alive}"


if __name__ == "__main__":
    doctest.testmod()
    pass
