import doctest


class Suitcase:
    def __init__(self, wheels_number: int, sections_number: int):
        """
        Создание и подготовка к работе объекта "Чемодан"

        :param wheels_number: Число колес, от 2 до 4
        :param sections_number: Число секций

        Примеры:
        >>> suitcase = Suitcase(2,3)    # инициализация экземпляра класса
        """
        if not isinstance(wheels_number, int):
            raise TypeError('Число колес должно быть целым')
        if not wheels_number > 0:
            raise ValueError('Число колес должно быть положительным')
        self.wheels_number = wheels_number

        if not isinstance(sections_number, int):
            raise TypeError('Число секций должно быть целым')
        if not sections_number > 0:
            raise ValueError('Число секций должно быть положительным')
        self.sections_number = sections_number

    def wheels_number_check(self) -> bool:
        """
        Функция проверяет, находится ли число колес в интервале от 2 до 4 включительно с обеих сторон.

        :return: Находится ли число колес в интервале от 2 до 4
        Примеры:
        suitcase = Suitcase(4, 5)
        suitcase.wheels_number_check()
        """
        ...

    def opened_sections_number(self, locked_sections: int) -> int:
        """
        Функция считает, сколько секций из общего числа нельзя закрыть на замок.

        :param locked_sections: Число закрываемых на замок секций
        :raise ValueError: Если число закрываемых секций меньше нуля или больше общего числа секций,
        то возвращается ошибка

        :return: Число открытых секций
        """
        ...


class Coat:
    def __init__(self, pockets_number: int, fabric: str):
        """
        Создание и подготовка к работе объекта "Пальто"

        :type fabric: Строка, чтобы записать наименование ткани
        :param pockets_number: Число карманов
        :param fabric: Ткань пальто

        Примеры:
        >>> coat = Coat(2,'wool')    # инициализация экземпляра класса
        """
        if not isinstance(pockets_number, int):
            raise TypeError('Число карманов должно быть целым')
        if pockets_number < 0:
            raise ValueError('Число карманов не должно быть отрицательным')
        self.pockets_number = pockets_number

        if not isinstance(fabric, str):
            raise TypeError('Ткань должна быть записана строкой')
        if len(fabric) == 0:
            raise ValueError('В ткани должны быть символы')
        self.fabric = fabric

    def pockets_number_check(self) -> bool:
        """
        Функция проверяет, хочет ли клиент иметь карманы на пальто.

        :return: Хочет ли клиент иметь карманы на пальто

        Примеры:
        coat = Coat(2,'wool')
        coat.pockets_number_check()
        """
        ...

    def is_fabric_available(self, catalogue: (list, tuple)) -> bool:
        """
        Функция проверяет, есть ли в каталоге запрошенная клиентом ткань.

        :param catalogue: Каталог, в котором ткани представлены списком или кортежом
        :raise TypeError: Если каталог представлен не списком или кортежом, то возвращается ошибка

        :return: Есть ли в каталоге запрошенная клиентом ткань

        Примеры:
        coat = Coat(2,'wool')
        coat.is_fabric_available(catalogue)
        """
        ...


class BankAccount:
    def __init__(self, account_number: int, deposit: (float, int)):
        """
            Создание и подготовка к работе объекта "Банковский счет"

            :param account_number: Номер банковского счета
            :param deposit: Депозит

            Примеры:
            >>> bank_account = BankAccount(20125,1000.6)    # инициализация экземпляра класса
        """
        if not isinstance(account_number, int):
            raise TypeError('Номер банковского счета должен быть целым')
        if not account_number > 0:
            raise ValueError('Номер банковского счета не должен быть отрицательным')
        self.account_number = account_number

        if not isinstance(deposit, (float, int)):
            raise TypeError('Депозит должен быть числом')
        if not deposit > 0:
            raise ValueError('Депозит не должен быть отрицательным')
        self.deposit = deposit

    def money_transfer(self, recipient_account_number: int, amount: (float, int)) -> None:
        """
        Функция переводит деньги с изначального банковского счета на счет получателя.

        :param recipient_account_number: Номер банковского счета получателя
        :param amount: Сумма перевода
        :raise ValueError: Сумма перевода больше депозита
        :raise ValueError: Сумма перевода не положительна

        Примеры:
        bank_account = BankAccount(20125,100.6)
        bank_account.money_transfer(10022,50)
        """
        ...

    def money_operation(self, money: (int, float)) -> None:
        """
        Функция добавляет деньги на счет или снимает ту же сумму со счета.

        :param money: Вносимая или снимаемая сумма денег (снимаемая сумма отрицательна)
        :raise TypeError: Если сумма денег не число, то возвращается ошибка
        :raise ValueError: Если сумма денег равно 0, то возвращается ошибка

        Примеры:
        bank_account = BankAccount(20125,100.6)
        bank_account.money_operation(-50)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
#
