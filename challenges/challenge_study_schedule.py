def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    for period in permanence_period:
        if type(period[0]) is not int or type(period[1]) is not int:
            return None
        if period[0] is None or period[1] is None:
            return None

    return 'Tudo ok!'

# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
# target_time = 5
# print(study_schedule(permanence_period, target_time))
