from typing_extensions import Self
from events_simulation import can_get_pregnancy, expected_number_of_childs


from variables_simulation import desease_age, wants_couple

class Person:
    def __init__(self, actual_age: int) -> None:
        self.actual_age = actual_age
        self.desease_age = desease_age(self.is_male, self.actual_age)
        self.has_couple = False
        self.couple: Person = None
        self.childs: int = 0
        self.expected_childs = expected_number_of_childs()
        self.is_dead = False
        self.wants_couple = wants_couple(self)

class Male(Person):
    def __init__(self, actual_age: int) -> None:
        super().__init__(actual_age)
        self.is_male: bool = True

class Female(Person):
    def __init__(self, actual_age: int) -> None:
        super().__init__(actual_age)
        self.is_male: bool = False
        self.is_pregnant = False
        self.can_get_pregnancy = can_get_pregnancy(self)