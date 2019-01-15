class User():
    """Класс пользователя."""
    __name = None
    __password = None
    _is_admin = False

    def __init__(self) -> None:
        pass
        # self.__name = name
        # self.set_password(password)
        # self._is_admin = is_admin

    def __str__(self):
        return self.name

    

    """
    getter через декоратор
    """
    @property
    def name(self) -> str:
        return self.__name

    """
    setter через декоратор
    """
    @name.setter
    def name(self, input_name: str) -> None:
        self.__name = input_name

    def password(self, password: str) -> None:
        self.__password = hash(password)


    """
    getter через свойство
    """
    def get_admin(self) -> bool:
        return self._is_admin
    
    """
    setter через свойство
    """
    def set_admin(self, is_admin: bool) -> None:
        self._is_admin = is_admin

    """
    связывание setter и getter свойством
    """
    is_admin = property(get_admin, set_admin)