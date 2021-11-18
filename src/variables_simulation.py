from random_variables_simulation import *
from person import Person

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
        if U <= desease_age_range_probs[i] and actual_age <= desease_age_ranges[1]:
            # return index of age range
            return i

    # return default age range index
    return 4

breakup_time_age_ranges = [(12,15), (16,21), (22,35), (36,45), (46,60), (61,125)]
breakup_time_parameter = [3, 6, 6, 12, 24, 48]

def after_breakup_time(person: Person):
    age = person.actual_age
    h = 48
    for i in range(len(breakup_time_age_ranges)):
        if age >= breakup_time_age_ranges[0] and age <= breakup_time_age_ranges[1]:
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

def wants_couple(person: Person):
    for i in range(len(want_couple_age_range)):
        if person.actual_age >= want_couple_age_range[i][0] and person.actual_age <= want_couple_age_range[i][1]:
            U = uniform(0, 1)

            return U <= want_couple_prob[i]
    
    return False