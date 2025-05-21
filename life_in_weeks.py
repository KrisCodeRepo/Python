def life_in_weeks(age):
    total_weeks = 90 * 52
    current_age_in_weeks = age * 52
    number_of_weeks_left = total_weeks - current_age_in_weeks
    print(f'You have {number_of_weeks_left} left.')

life_in_weeks(56)