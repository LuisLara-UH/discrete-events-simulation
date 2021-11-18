from event import AfterBreakup, BirthDay, Birth, Breakup
from person import Person, Male, Female
from random_variables_simulation import exponential, uniform
from variables_simulation import *

def simulate_birth(date: int, mother: Female, father: Male, population: list):
    events = []

    if mother.is_dead:
        return []

    childs = birth_childs()
    for _ in range(childs):
        child = Person(0)
        population.append(child)
        events.append(BirthDay(date + 12, child))

    mother.is_pregnant = False
    mother.childs += childs
    father.childs += childs

    return events

age_ranges_start = [12, 16, 22, 36, 46, 61]

def simulate_birthday(date: int, person: Person, poblation: list):
    if person.is_dead:
        return []

    person.actual_age += 1

    events = []
    events.append(BirthDay(date + 12, person))

    for age in age_ranges_start:
        if person.actual_age == age:
            if not person.has_couple:
                person.wants_couple = wants_couple(person)
            if not person.is_male:
                person.can_get_pregnancy = can_get_pregnancy(person)

    if not person.has_couple:
        events += simulate_partner_search(date, person, poblation)

    return events

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

            if posible_pregnancy(girlfriend):
                girlfriend.is_pregnant = True
                events.append(Birth(date, mother=girlfriend, father=boyfriend))

            return events

def simulate_desease(date: int, person: Person):
    person.is_dead = True
    if person.has_couple:
        return simulate_breakup(date, person, person.couple)

    return []

def simulate_breakup(date: int, person1: Person, person2: Person):
    person1.has_couple = False
    person2.has_couple = False

    person1.couple = None
    person2.couple = None

    after_breakups = []

    if not person1.is_dead:
        after_breakups.append(AfterBreakup(date + after_breakup_time(person1), person1))

    if not person2.is_dead:
        after_breakups.append(AfterBreakup(date + after_breakup_time(person2), person2))

    return after_breakups

def simulate_after_breakup(date: int, person: Person, poblation: list):
    if person.is_dead:
        return []
    
    person.wants_couple = wants_couple(person)

    return simulate_partner_search(date, person, poblation)