from random_variables_simulation import *

desease_age_ranges = [(0,12), (13,45), (46,76), (77,125)]

desease_age_range_probs_male = [0.25, 0.1, 0.3, 0.7]
desease_age_range_probs_female = [0.25, 0.15, 0.35, 0.65]

def desease_age(male: bool, actual_age: int):
    age_range_index = desease_range_age(male, actual_age)

    # default desease age
    age = 126

    if age_range_index < 4:
        age_range = desease_age_ranges[age_range_index]
        age = uniform(age_range[0], age_range[1])

    return age

def desease_range_age(male: bool, actual_age):
    if male:
        desease_age_range_probs = desease_age_range_probs_male
    else:
        desease_age_range_probs = desease_age_range_probs_female

    for i in range(4):
        U = uniform(0, 1)
        if U <= desease_age_range_probs[i] and actual_age <= desease_age_ranges[i][0]:
            # return index of age range
            return i

    # return default age range index
    return 4

breakup_time_age_ranges = [(12,15), (16,21), (22,35), (36,45), (46,60), (61,125)]
breakup_time_parameter = [3, 6, 6, 12, 24, 48]

def after_breakup_time(person):
    age = person.actual_age
    h = 48
    for i in range(len(breakup_time_age_ranges)):
        if age >= breakup_time_age_ranges[i][0] and age <= breakup_time_age_ranges[i][1]:
            h = breakup_time_parameter[i]

    return int(exponential(h))


expected_number_of_childs_probs = [0.6, 0.75, 0.35, 0.2, 0.1, 0.05]

def expected_number_of_childs():
    for i in range(len(expected_number_of_childs_probs)):
        U = uniform(0, 1)
        if U <= expected_number_of_childs_probs[i]:
            return (i + 1)

    return 0

want_couple_age_range = [(12,15), (16,21), (22,35), (36,45), (46,60), (61,125)]
want_couple_prob = [0.6, 0.65, 0.8, 0.6, 0.5, 0.2]

def wants_couple(person):
    for i in range(len(want_couple_age_range)):
        if person.actual_age >= want_couple_age_range[i][0] and person.actual_age <= want_couple_age_range[i][1]:
            U = uniform(0, 1)

            return U <= want_couple_prob[i]
    
    return False


pregnancy_age_ranges = [(12,15), (16,21), (22,35), (36,45), (46,60), (61,125)]
pregnancy_probs = [0.2, 0.45, 0.8, 0.4, 0.2, 0.05]

def posible_pregnancy(female):
    if (not female.has_couple) or (not female.can_get_pregnancy) or female.is_pregnant:
        return False

    if female.childs > female.expected_childs or female.couple.childs > female.couple.expected_childs:
        return False

    return True

def can_get_pregnancy(person):
    for i in range(len(pregnancy_age_ranges)):
        if person.actual_age >= pregnancy_age_ranges[i][0] and person.actual_age <= pregnancy_age_ranges[i][0]:
            U = uniform(0, 1)
            return U <= pregnancy_probs[i]

    return False

age_difference_ranges = [(0,5), (6,10), (11, 15), (16, 20), (21,126)]
get_partner_prob = [0.45, 0.40, 0.35, 0.25, 0.15]

def relationship(person1, person2):
    if not ((person1.is_male and not person2.is_male) or (not person1.is_male and person2.is_male)):
        return False

    if person1.is_dead or person2.is_dead:
        return False

    if not person1.wants_couple or not person2.wants_couple:
        return False

    if person1.has_couple or person2.has_couple:
        return False

    age_difference = person1.actual_age - person2.actual_age
    if age_difference < 0:
        age_difference = age_difference * (-1)

    for i in range(len(age_difference_ranges)):
        if age_difference <= age_difference_ranges[i][1]:
            U = uniform(0, 1)
            return U <= get_partner_prob[i]

    return False

def breakup():
    U = uniform(0, 1)
    return U <= 0.2

def time_to_breakup():
    return uniform(1, 12*50)

birth_childs_prob = [0.7, 0.18, 0.06, 0.04, 0.02]

def birth_childs() -> int:
    U = uniform(0, 1)
    for i in range(5):
        if U <= birth_childs_prob[i]:
            return i + 1
        U -= birth_childs_prob[i]

    return 1