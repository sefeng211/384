'''
The main program for CSC384 project
'''
from cspModel import *
from cspbase import *
from propagators import *
from orderings import *
WELCOME_MESSAGE = "Thanks for using IMeal"
ASK_MEAL_NUM = "Enter number of days you want to generated: "
ASK_PROTEIN = "Enter how much protein do you want to have per day: "
ASK_SUGAR = "Enter how much sugar do you want to have per day: "
ASK_CALCIUM = "Enter how much calcium do you want to have per day: "
ASK_BUDGET = "Enter a budget limitation per day: "
ASK_SPECIAL_REQUEST = "You can select some special request: "
SPECIAL_REQUESTS = ["1.Reduce repeated meals",
                    "2.Eat as much as I can",
                    "3.I am special request 3"]

MOCK_FOOD_DATA = {
        'cheese':
            {
                'water': 1,
                'energy': 2,
                'protein': 3,
                'sugar': 5,
                'calcium': 1,
                'budget': 10
            },
        'Cool':
            {
                'water': 1,
                'energy': 2,
                'protein': 1,
                'sugar': 5,
                'calcium': 1,
                'budget': 10
            },
        'Milk':
            {
                'water': 1,
                'energy': 2,
                'protein': 3,
                'sugar': 2,
                'calcium': 1,
                'budget': 6
            },
        'Bread':
            {
                'water': 1,
                'energy': 2,
                'protein': 3,
                'sugar': 1,
                'calcium': 2,
                'budget': 4
            }
    }
def main():
    """
    The main function
    """
    # TODO: This function should print the necessary information to the shell
    # and collect information from the user, then invoke functions to output a
    # meal to the user
    # We need to ask:
    #   1) Calorie goals
    #   2) Number of meals to be generated
    #   3）Nutrition amount per meal/day/plan
    #   4) Budget
    #   5) Special Considerations such as "no two idential meals in a day" or
    # "vegetarian" and etc
    print(WELCOME_MESSAGE)
    while True:
        try:
            days = int(input(ASK_MEAL_NUM))
            protein = int(input(ASK_PROTEIN))
            sugar = int(input(ASK_SUGAR))
            calcium = int(input(ASK_CALCIUM))
            budget = int(input(ASK_BUDGET))
        except ValueError:
            print("Sorry please enter a number or None")
        print(ASK_SPECIAL_REQUEST)
        for request in SPECIAL_REQUESTS:
            print(request)
        while True:
            r_input = input()
            requests = r_input.split()
            passed = 0
            requests = list(map(int, requests))
            for r in requests:
                if not isinstance(r, int):
                    print("Please enter the number you want")
                    passed = 1
            if passed == 0:
                break
        break
    start(days, protein, sugar, calcium, budget, requests)

def start(num_days, protein, sugar, calcium, budget, special_requests):
    '''
    Start the progress to make the meals for user
    :param num_meal: Number of meals
    :param protein: Amount of protein
    :param sugar: Amount of sugar
    :param calcium: Amount of calcium
    :param budget: budget
    :param special_requests: Some special requests that the user may have
    :return: The meals that the CSP generated
    '''

    user_input_data = {
        'days': num_days,
        'protein': protein,
        'sugar': sugar,
        'calcium': calcium,
        'budget': budget,
        'special_requests': special_requests
    }
    ordering_function = val_arbitrary
    if 2 in special_requests:
        EAT_AS_MUSH_AS_I_CAN = True
        ordering_function = val_odering_max_protein


    # food_data = create_food_data()
    csp_modle, var_array = IMeal_Model(user_input_data, MOCK_FOOD_DATA)
    solver = BT(csp_modle)
    solver.bt_search(prop_BT, ord_mrv,
                     ordering_function)

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
        day_counter += 1

if __name__ == '__main__':
    # main()
    start(1, 10, 100, 10, 1000, [2])