from person import Female, Person, Male
from events_simulation import *

class Event:
    def __init__(self, date: int) -> None:
        self.date = date

    def execute(self):
        pass

class Birth(Event):
    def __init__(self, date: int, mother: Female, father: Male) -> None:
        super().__init__(date)
        self.mother = mother
        self.father = father

    def execute(self, poblation: list):
        return simulate_birth(self.date, self.mother, self.father, poblation)


class BirthDay(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self, poblation: list):
        return simulate_birthday(self.date, self.person, poblation)

class Desease(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self):
        return simulate_desease(self.date, self.person)


class Breakup(Event):
    def __init__(self, date: int, girlfriend: Female, boyfriend: Male) -> None:
        super().__init__(date)
        self. girlfriend = girlfriend
        self.boyfriend = boyfriend

    def execute(self):
        return simulate_breakup(self.date, self.boyfriend, self.girlfriend)

class AfterBreakup(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self):
        return simulate_after_breakup(self.date, self.person)