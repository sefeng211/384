'''
The main program for CSC384 project
'''
from cspModel import IMeal_Model

WELCOME_MESSAGE = "Thanks for using IMeal"
ASK_MEAL_NUM = "Enter number of meals you want to generated: "
ASK_PROTEIN = "Enter how much protein do you want to have: "
ASK_SUGAR = "Enter how much sugar do you want to have: "
ASK_CALCIUM = "Enter how much calcium do you want to have: "
ASK_BUDGET = "Enter a budget limitation: "
ASK_SPECIAL_REQUEST = "You can select some special request: "
SPECIAL_REQUESTS = ["1.I am special request 1",
                    "2.I am special request 2",
                    "3.I am special request 3"]

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
            meals = int(input(ASK_MEAL_NUM))
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
    start(meals, protein, sugar, calcium, budget, requests)

def start(num_meal, protein, sugar, calcium, budget, special_requests):
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
        'num_meals': num_meal,
        'protein': protein,
        'sugar': sugar,
        'calcium:': calcium,
        'budget': budget,
        'special_requests': special_requests
    }

    csp_modle = IMeal_Model(user_input_data)
    pass

if __name__ == '__main__':
    main()