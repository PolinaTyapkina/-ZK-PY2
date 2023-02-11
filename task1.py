if __name__ == "__main__":
    class MusicInstrument:
        """Базовый класс - музыкальный инструмент"""

        def __init__(self, name: str, material: str):
            self.name = name  # protected, чтобы проверить тип вводимых данных
            self.material = material  # protected, чтобы проверить тип вводимых данных

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}. material = {self.material!r}'

        def __str__(self) -> str:
            return f'Муз.инструмент "{self.name}". Материал "{self.material}"'

        @property
        def name(self) -> str:
            return self._name

        @name.setter
        def name(self, name: str) -> None:
            if not isinstance(name, str):
                raise TypeError('Неверен тип данных для наименования инструмента')
            self._name = name

        @property
        def material(self) -> str:
            return self._material

        @material.setter
        def material(self, material: str) -> None:
            if not isinstance(material, str):
                raise TypeError('Неверен тип данных для основного материала')
            self._material = material

        def music_school(self, catalogue: (list, tuple)) -> bool:
            """
            Функция проверяет, есть ли в каталоге изучаемых в муз.школе инструментов указанный инструмент.
            Перегрузка функции при наследовании не требуется.

            :param catalogue: Каталог, в котором доступные инструменты представлены списком или кортежом
            :raise TypeError: Если каталог представлен не списком или кортежом, то возвращается ошибка

            :return: Есть ли в каталоге запрошенный инструмент

            Примеры:
            instrument = MusicInstrument('Guitar','Wood')
            instrument.music_school(catalogue)
            """
            ...

        def care_instructions(self, instructions: dict) -> dict:
            """
            Функция выдает словарь рекомендаций для всех материалов. Если материал один,
            то выдается только одна пара ключ-значение.
            :param instructions: Словарь с инструкциями для возможных материалов
            :return: Рекомендации по уходу за материалом

            Примеры:
            instrument = MusicInstrument('Guitar','Wood')
            instrument.care_instructions(instructions)
            """
            ...


    class Guitar(MusicInstrument):
        """
        Дочерний класс, в котором больше аргументов: появляется material_string - материал струн.
        Перегрузка функции music_school при наследовании не требуется.
        Перегрузка функции care_instructions требуется, т.к. появился второй материал.
        """

        def __init__(self, name: str, material: str, material_string: str):
            super().__init__(name, material)
            self.material_string = material_string

        def __repr__(self) -> str:
            return f'{self.__class__.__name__}({self.name!r}. material = {self.material!r}. ' \
                   f'material_string = {self.material_string!r}'

        def __str__(self) -> str:
            return f'Гитара "{self.name}". Основной материал "{self.material}". ' \
                   f'Материал струн "{self.material_string}"'

        @property
        def material_string(self) -> str:
            return self._material_string

        @material_string.setter
        def material_string(self, material_string: str) -> None:
            if not isinstance(material_string, str):
                raise TypeError('Неверен тип данных для материала струн')
            self._material_string = material_string

        def care_instructions(self, instructions: dict) -> dict:
            super().care_instructions(instructions)
            """
            Добавить вывод рекомендаций и для нового атрибута material_string, чтобы функция
            выдавала словарь для всех материалов (material и material_string).
            """
            ...
    pass
#
