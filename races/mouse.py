class Mouse:
    def __init__(self, name: str, speed: float, stamina: float, preference: str,
                 daily_well_being: float):
        self.name = name
        self.speed = speed
        self.stamina = stamina
        self.preference = preference
        self.daily_well_being = daily_well_being

    def __str__(self):
        return f"{self.name}, {self.speed}, {self.stamina}, {self.preference}, {self.daily_well_being}"

    def get_name(self) -> str:
        return self.name

    def get_speed(self) -> float:
        return self.speed

    def get_stamina(self) -> float:
        return self.stamina

    def get_preference(self) -> str:
        return self.preference

    def get_daily_well_being(self) -> float:
        return self.daily_well_being
