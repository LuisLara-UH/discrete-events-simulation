from variables_simulation import *
from person import Person, Male, Female

def simulate_partner_search(date: int, person: Person, poblation: list):
    if person.is_dead:
        return []

    events = []

    for posible_partner in poblation:
        if relationship(person, posible_partner):
            person.has_couple = True
            person.couple = posible_partner

            posible_partner.has_couple = True
            posible_partner.couple = person

            girlfriend = person
            boyfriend = posible_partner
            if person.is_male:
                boyfriend = person
                girlfriend = posible_partner

            if breakup():
                events.append(Breakup(time_to_breakup(), girlfriend, boyfriend))
            
            print_event_relationship(date, person, posible_partner)

            events += simulate_posible_pregnancy(date, girlfriend)

            return events

    return []

def print_event_relationship(date: int, person1, person2):
    print()
    print('Event: Relationship')
    print('Date:', date)
    print('Person 1:', person1.id, ',is male', person1.is_male)
    print('Person 2:', person2.id, ',is male', person2.is_male)

def simulate_posible_pregnancy(date, mother):
    if posible_pregnancy(mother):
        mother.is_pregnant = True
        print_event_pregnancy(date, mother, mother.couple)
        return [Birth(date, mother=mother, father=mother.couple)]

    return []

def print_event_pregnancy(date: int, mother, father):
    print()
    print('Event: Pregnancy')
    print('Date:', date)
    print('Mother:', mother.id)
    print('Father:', father.id)

class Event:
    def __init__(self, date: int) -> None:
        self.date = date

    def execute(self, poblation: list):
        pass

    def print_event(self):
        pass

class Birth(Event):
    def __init__(self, date: int, mother: Female, father: Male) -> None:
        super().__init__(date)
        self.mother = mother
        self.father = father
        self.childs = []

    def execute(self, poblation: list):
        events = []

        if self.mother.is_dead:
            return []

        childs = birth_childs()
        for _ in range(childs):
            U = uniform(0, 1)
            if U <= 0.5:
                child = Male(len(poblation), 0)
            else:
                child = Female(len(poblation), 0)

            self.childs.append(child)
            poblation.append(child)
            events.append(BirthDay(self.date + 12, child))
            events.append(Desease(self.date + (desease_age(child.is_male, 0) * 12), child))

        self.mother.is_pregnant = False
        self.mother.childs += childs
        self.father.childs += childs

        events += simulate_posible_pregnancy(self.date, self.mother)

        return events

    def print_event(self):
        print()
        print('Event: Birth')
        print('Date:', self.date)
        print('Mother:', self.mother.id)
        print('Father:', self.father.id)
        print('Childs:', (child.id + ' ' for child in self.childs))

class BirthDay(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person
        self.age_ranges_start = [12, 16, 22, 36, 46, 61]

    def execute(self, poblation: list):
        if self.person.is_dead:
            return []

        self.person.actual_age += 12

        events = []
        events.append(BirthDay(self.date + 12, self.person))

        if not self.person.has_couple:
            self.person.wants_couple = wants_couple(self.person)
            events += simulate_partner_search(self.date, self.person, poblation)
        elif not self.person.is_male:
            events += simulate_posible_pregnancy(self.date, self.person)

        return events

    def print_event(self):
        """
        print()
        print('Event: Birthday')
        print('Date:', self.date)
        print('Person:', self.person.id)
        print('Is male:', self.person.is_male)
        print('New age:', self.person.actual_age)
        """

class Desease(Event):
    def __init__(self, date: int, person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self, poblation: list):
        self.person.is_dead = True

        if self.person.has_couple:
            breakup_event = Breakup(self.date, self.person, self.person.couple)
            return breakup_event.execute(poblation)

        return []

    def print_event(self):
        print()
        print('Event: Desease')
        print('Date:', self.date)
        print('Person:', self.person.id)
        print('Age', self.person.actual_age)
        print('Is male:', self.person.is_male)

class Breakup(Event):
    def __init__(self, date: int, person1: Person, person2: Person) -> None:
        super().__init__(date)
        self.person1 = person1
        self.person2 = person2

    def execute(self, poblation: list):
        self.person1.has_couple = False
        self.person2.has_couple = False

        self.person1.couple = None
        self.person2.couple = None

        after_breakups = []

        if not self.person1.is_dead:
            after_breakups.append(AfterBreakup(self.date + after_breakup_time(self.person1), self.person1))

        if not self.person2.is_dead:
            after_breakups.append(AfterBreakup(self.date + after_breakup_time(self.person2), self.person2))

        return after_breakups

    def print_event(self):
        print()
        print('Event: Breakup')
        print('Date:', self.date)
        print('Person1:', self.person1.id, 'is male:', self.person1.is_male)
        print('Person2:', self.person2.id, 'is male:', self.person2.is_male)

class AfterBreakup(Event):
    def __init__(self, date: int, person: Person) -> None:
        super().__init__(date)
        self.person = person

    def execute(self, poblation: list):
        if self.person.is_dead:
            return []

        return simulate_partner_search(self.date, self.person, poblation)

    def print_event(self):
        print()
        print('Event: After Breakup')
        print('Date:', self.date)
        print('Person:', self.person.id)
        print('Is male:', self.person.is_male)