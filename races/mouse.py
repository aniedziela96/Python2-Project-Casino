class Mouse:
    """
    A class used to represent a mouse (for races).

    :param name: The name of the mouse
    :type name: str
    :param speed: The speed of the mouse
    :type speed: float
    :param stamina: The stamina of the mouse
    :type stamina: float
    :param preference: The track preference of the mouse
    :type name: str
    :param daily_well_being: The daily well-being of the mouse
    :type name: float
    """
    def __init__(self, name: str, speed: float, stamina: float, preference: str,
                 daily_well_being: float) -> None:
        """
        Constructor method.
        """
        self.name = name
        self.speed = speed
        self.stamina = stamina
        self.preference = preference
        self.daily_well_being = daily_well_being

    def __str__(self) -> str:
        return f"{self.name}, {self.speed}, {self.stamina}, {self.preference}, {self.daily_well_being}"

    def get_name(self) -> str:
        """
        Name's getter.

        :return: The name of the mouse
        :rtype: str
        """
        return self.name

    def get_speed(self) -> float:
        """
        Speed's getter.

        :return: The speed of the mouse
        :rtype: float
        """
        return self.speed

    def get_stamina(self) -> float:
        """
        Stamina's getter.

        :return: The stamina of the mouse
        :rtype: float
        """
        return self.stamina

    def get_preference(self) -> str:
        """
        Preference's getter.

        :return: The track preference of the mouse
        :rtype: str
        """
        return self.preference

    def get_daily_well_being(self) -> float:
        """
        Daily well-being's getter.

        :return: The daily well-being of the mouse
        :rtype: float
        """
        return self.daily_well_being
