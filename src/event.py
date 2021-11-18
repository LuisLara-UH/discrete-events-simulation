from person import Female, Person, Male

class Event:
    def __init__(self, date: int) -> None:
        self.date = date

    def execute(self):
        pass

class GetPregnant(Event):
    def __init__(self, date: int, mother: Female, father: Male) -> None:
        super().__init__(date)
        self.mother = mother
        self.father = father

    def execute(self):
        if self.father.is_dead or self.mother.is_dead:
            return []

        self.mother.is_pregnant = True
        birth = Birth(self.date, mother=self.mother, father=self.father)

        return [birth]

class Birth(Event):
    def __init__(self, date: int, mother: Female, father: Male) -> None:
        super().__init__(date)
        self.mother = mother
        self.father = father

    def execute(self, population: list):
        if self.mother.is_dead:
            return []

        child = Person(0)
        population.append(child)
        self.mother.childs += 1
        self.father.childs += 1

        birthday = BirthDay(self.date + 12, child)
        return [birthday]


class BirthDay(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self):
        if self.person.is_dead:
            return []

        ### Fill

        return [BirthDay(self.date + 12, self.person)]

class Desease(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self):
        self.person.is_dead = True
        if self.person.has_couple:
            couple = self.person.couple
            couple.has_couple = False
            couple.couple = None

        return []

class Relationship(Event):
    def __init__(self, date: int, girlfriend: Female, boyfriend: Male) -> None:
        super().__init__(date)
        self. girlfriend = girlfriend
        self.boyfriend = boyfriend

    def execute(self):
        return super().execute()

class Breakup(Event):
    def __init__(self, date: int, girlfriend: Female, boyfriend: Male) -> None:
        super().__init__(date)
        self. girlfriend = girlfriend
        self.boyfriend = boyfriend

    def execute(self):
        return super().execute()

class AfterBreakup(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self):
        return super().execute()