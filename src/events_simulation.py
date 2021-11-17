from variables_simulation import *

desease_age_ranges = [(0,12), (13,45), (46,76), (77,125)]

desease_age_range_probs_male = [0.25, 0.1, 0.3, 0.7]
desease_age_range_probs_female = [0.25, 0.15, 0.35, 0.65]

def desease_age(male: bool):
    age_range_index = desease_range_age(male)

    # default desease age
    age = 126

    if age_range_index < 4:
        age_range = desease_age_ranges[age_range_index]
        age = uniform(age_range[0], age_range[1])

    return age

def desease_range_age(male: bool):
    if male:
        desease_age_range_probs = desease_age_range_probs_male
    else:
        desease_age_range_probs = desease_age_range_probs_female

    for i in range(4):
        U = uniform(0, 1)
        if U <= desease_age_range_probs[i]:
            # return index of age range
            return i

    # return default age range index
    return 4