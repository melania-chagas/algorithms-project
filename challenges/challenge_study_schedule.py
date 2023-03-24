def parameter_validation(permanence_period, target_time):
    if not target_time:
        return None

    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None
        if period[0] is None or period[1] is None:
            return None

    return 'Tudo ok!'


def study_schedule(permanence_period, target_time):
    if parameter_validation(permanence_period, target_time) == 'Tudo ok!':
        number_of_students = 0
        for period in permanence_period:
            if period[0] == target_time:
                number_of_students += 1
            if target_time > period[0] and target_time <= period[1]:
                number_of_students += 1

        return number_of_students


# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target_time = 5
# print(study_schedule(permanence_period, target_time))
