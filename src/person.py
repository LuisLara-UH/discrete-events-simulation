from variables_simulation import desease_age, wants_couple, can_get_pregnancy, expected_number_of_childs

class Person:
    def __init__(self, id: int, actual_age: int) -> None:
        self.id = id
        self.actual_age = actual_age
        self.desease_age = desease_age(self.is_male, self.actual_age)
        self.has_couple = False
        self.couple: Person = None
        self.childs: int = 0
        self.expected_childs = expected_number_of_childs()
        self.is_dead = False
        self.wants_couple = wants_couple(self)

class Male(Person):
    def __init__(self, id: int, actual_age: int) -> None:
        self.is_male: bool = True
        super().__init__(id, actual_age)

class Female(Person):
    def __init__(self, id: int, actual_age: int) -> None:
        self.is_male: bool = False
        self.is_pregnant = False
        super().__init__(id, actual_age)
        self.can_get_pregnancy = can_get_pregnancy(self)