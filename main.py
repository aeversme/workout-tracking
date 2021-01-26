import operations as ops


def workout_tracker():
    user_data, exercise_input = ops.user_inputs()
    exercises_list = ops.nutritionix_api(user_data, exercise_input)
    ops.sheety_api(exercises_list)


workout_tracker()
