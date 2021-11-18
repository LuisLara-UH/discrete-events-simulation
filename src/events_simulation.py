from person import Person, Male, Female
from random_variables_simulation import exponential, uniform

pregnancy_age_ranges = [(12,15), (16,21), (22,35), (36,45), (46,60), (61,125)]
pregnancy_probs = [0.2, 0.45, 0.8, 0.4, 0.2, 0.05]


def posible_pregnancy(female: Female):
    if not female.has_couple or female.couple is None or not female.can_get_pregnancy or female.is_pregnant:
        return False

    if female.childs > female.expected_childs or female.couple.childs > female.couple.expected_childs:
        return False

    return True

def can_get_pregnancy(person: Female):
    for i in range(len(pregnancy_age_ranges)):
        if person.actual_age >= pregnancy_age_ranges[i][0] and person.actual_age <= pregnancy_age_ranges[i][0]:
            U = uniform(0, 1)
            return U <= pregnancy_probs[i]

    return False

age_difference_ranges = [(0,5), (6,10), (11, 15), (16, 20), (21,126)]
get_partner_prob = [0.45, 0.40, 0.35, 0.25, 0.15]

def simulate_partner_search(person: Person, poblation: list):
    for posible_partner in poblation:
        pass

def relationship(person1: Person, person2: Person):
    if not ((person1.is_male and not person2.is_male) or (not person1.is_male and person2.is_male)):
        return False

    if person1.is_dead or person2.is_dead:
        return False
