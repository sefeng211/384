'''
The main program for CSC384 project
'''
from cspModel import *
from cspbase import *
from propagators import *
from orderings import *
import collections

from process_db import *

WELCOME_MESSAGE = "Thanks for using IMeal"
ASK_MEAL_NUM = "Enter number of days you want to generated: "
ASK_ENERGY = "Enter how much energy/calories do " \
            "you want to have per day: "
ASK_PROTEIN = "Enter how much protein do you want to have per day: "
ASK_SUGAR = "Enter how much sugar do you want to have per day: "
ASK_CALCIUM = "Enter how much calcium do you want to have per day: "
ASK_BUDGET = "Enter a budget limitation per day: "
ASK_SPECIAL_REQUEST = "You can select some special request: "
CHOICE_SPECIAL_REQUESTS = ["Do you want to reduce repeated meals",
                            "Do you want to eat as much as you can"]
EAT_AS_MUCH_AS_I_CAN = 2
REDUCE_REPEATED_MEALS = 1

DATA_FILE = 'food_nutrition_small_v2.csv'

def main():
    """
    The main function
    """
    # This function should print the necessary information to the shell
    # and collect information from the user, then invoke functions to output a
    # meal to the user
    # We need to ask:
    #   1) Nutrition goals
    #   2) Number of days to be generated
    #   3）Nutrition amount per day
    #   4) Budget
    #   5) Special Considerations such as "no two idential meals in a day" or
    # "vegetarian" and etc
    print(WELCOME_MESSAGE)
    # Ask days
    while True:
        days = input(ASK_MEAL_NUM)

        try:
            days = int(days)
            break
        except ValueError:
            print("Sorry please enter a number or leave it empty")

    # Ask energy
    while True:
        energy = input(ASK_ENERGY)
        if energy =='':
            energy = None
            break
        else:
            try:
                energy = int(energy)
                break
            except ValueError:
                print("Sorry please enter a number or leave it empty")

    # Ask protein
    while True:
        protein = input(ASK_PROTEIN)
        if protein =='':
            protein = None
            break
        else:
            try:
                protein = int(protein)
                break
            except ValueError:
                print("Sorry please enter a number or leave it empty")

    # Ask sugar
    while True:
        sugar = input(ASK_SUGAR)
        if sugar =='':
            sugar = None
            break
        else:
            try:
                sugar = int(sugar)
                break
            except ValueError:
                print("Sorry please enter a number or leave it empty")

    # Ask calcium
    while True:
        calcium = input(ASK_CALCIUM)
        if calcium =='':
            calcium = None
            break
        else:
            try:
                calcium = int(calcium)
                break
            except ValueError:
                print("Sorry please enter a number or leave it empty")

    # Ask budget
    while True:
        budget = input(ASK_BUDGET)
        if budget =='':
            budget = None
            break
        else:
            try:
                budget = int(budget)
                break
            except ValueError:
                print("Sorry please enter a number or leave it empty")

    # Ask special requests
    while True:
        print(ASK_SPECIAL_REQUEST)
        requests = []
        request_counter = 1
        for request in CHOICE_SPECIAL_REQUESTS:
            print(request)
            while True:
                r_input = input()
                if r_input == 'Yes' or r_input == 'yes':
                    requests.append(request_counter)
                    request_counter += 1
                    break

                elif r_input != 'No' and r_input != 'no' and r_input != '':
                    print("Please enter Yes/No or leave it empty")
                else:
                    request_counter += 1
                    break
        break

    start(days, energy, protein, sugar, calcium, budget, requests)


def start(num_days, energy, protein, sugar, calcium, budget, special_requests):
    '''
    Start the progress to make the meals for user
    :param num_meal: Number of meals
    :param energy: Number of energy
    :param protein: Amount of protein
    :param sugar: Amount of sugar
    :param calcium: Amount of calcium
    :param budget: budget
    :param special_requests: Some special requests that the user may have
    :return: The meals that the CSP generated
    '''
    print("Start generating meals")
    user_input_data = {
        DAYS: num_days,
        ENERGY: energy,
        PROTEIN: protein,
        SUGAR: sugar,
        CALCIUM: calcium,
        BUDGET: budget,
        SPECIAL_REQUESTS: special_requests
    }
    ordering_function = val_arbitrary
    if EAT_AS_MUCH_AS_I_CAN in special_requests:
        ordering_function = val_odering_max
    data = csv_to_dict(DATA_FILE)
    orderd_data = collections.OrderedDict(data)
    repeated_request = True if REDUCE_REPEATED_MEALS \
                               in special_requests else False

    # food_data = create_food_data()
    csp_modle, var_array = IMeal_Model(user_input_data, orderd_data, repeated_request)
    solver = MealBT(csp_modle)
    solver.bt_search(prop_BT, ord_mrv,
                     ordering_function)
    success = solver.get_status()
    if not success:
        print("Sorry, we can't generate satisfied meals for your requirements")
    else:
        print_result(var_array)


def print_result(var_array):

    splited_into_days = split_meals_into_days(var_array)
    day_counter = 1
    for meals in splited_into_days:
        print("==============Day {} =============".format(str(day_counter)))
        meal_counter = 1
        for meal in meals:
            print("Meal {}".format(str(meal_counter)))
            for food in meal.get_assigned_value():
                print(food.get_name())

            meal_counter += 1
        calculate_nutrition(meals, PROTEIN)
        calculate_nutrition(meals, SUGAR)
        calculate_nutrition(meals, CALCIUM)
        calculate_nutrition(meals, BUDGET)
        calculate_nutrition(meals, ENERGY)
        day_counter += 1


def calculate_nutrition(var_array, type):

    sum = 0
    for meal in var_array:
        for food in meal.get_assigned_value():
            sum += food.get_amount(type)
    print("Total amount of {} is {}".format(type, sum))


if __name__ == '__main__':
    main()
    #
    # days = 10
    # protein = 300
    # energy = 3000
    # sugar = 300
    # calcium = 2000
    # budget = 1000
    # special_requests = [1, 2]
    # start(days, energy, protein, sugar, calcium, budget, special_requests)
