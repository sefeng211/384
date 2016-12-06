'''
The main program for CSC384 project
'''

WELCOME_MESSAGE = "Thanks for using IMeal"
ASK_CALORIE = "Enter how much calories do you want to have: "
ASK_NUTATION_PER_MEAL = "Enter how much nutrition do you want to have per meal: "
BUDGET = "Enter a budget limitation: "
SPECIAL_CONSIDERATION = "Select a special request: "
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
            calories = int(input(ASK_CALORIE))
        except ValueError:
            print("Sorry please enter a number or None")


    pass


if __name__ == '__main__':
    main()