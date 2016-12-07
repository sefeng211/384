from cspbase import *
from cspbaseMeal import *
import itertools
import collections
from itertools import chain, combinations
'''
Construct and return CSP model for IMeal.
'''

'''
This is taken from
https://docs.python.org/3/library/itertools.html#recipes
'''
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))

NUM_MEALS_PER_DAY = 3

PROTEIN = 'protein'
SUGAR = 'sugar'
CALCIUM = 'calcium'
BUDGET = 'budget'
DAYS = 'days'


def IMeal_Model(user_input_dic, food_data):
    '''
    Construct and return CSP model for IMeal.
    :param user_input_dic: A dictionary that contains all user input information
    :return: return a CSP Model for IMeal
    '''

    csp = MealCSP('IMeal_model', [])
    num_meals = user_input_dic[DAYS] * NUM_MEALS_PER_DAY
    protein = user_input_dic[PROTEIN]
    sugar = user_input_dic[SUGAR]
    calcium = user_input_dic[CALCIUM]
    budget = user_input_dic[BUDGET]

    # Each meal plan will be a variable
    for i in range(0, num_meals):
        variable_name = 'Meal_'+ str(i)
        # The domain of each varialbe will be the food selection
        var_domain = create_domain(food_data)
        var = MealPlanVariable(variable_name, var_domain)
        csp.add_var(var)

    # Protein Constraint
    meals_in_days = split_meals_into_days(csp.get_all_vars())
    day_counter = 1
    for meal_in_day in meals_in_days:
        c = Constraint("Protein_Day_{}".format(day_counter),
                       meal_in_day)
        day_counter += 1
        all_possible_tuples = find_possible_tuples(PROTEIN, protein, meal_in_day)
        c.add_satisfying_tuples(all_possible_tuples)
        csp.add_constraint(c)

    # Sugar Constraint
    # day_counter = 1
    # for meal_in_day in meals_in_days:
    #     c = Constraint("Sugar_Day_{}".format(day_counter),
    #                    meal_in_day)
    #     day_counter += 1
    #     all_possible_tuples = find_possible_tuples(SUGAR, sugar, meal_in_day)
    #     c.add_satisfying_tuples(all_possible_tuples)
    #     csp.add_constraint(c)

    # Calcium Constraint


    # Budget Constraint


    return csp, csp.get_all_vars()

def create_domain(food_data):
    '''
    create the domain for variables based on the input food data
    :param food_data: The possible food selection
    Assume the food_data is in this format
    {
        'cheese':
            {
                'water': 1,
                'energy': 1,
                'protein': 1
            },
        'Milk':
            {
                'water': 1,
                'energy': 1,
                'protein': 1
            },
        'Bread':
            {
                'water': 1,
                'energy': 1,
                'protein': 1
            }
    }
    :return: a power set of input food_data
    Example
    [[Food(Cheese)],
     [Food(Cheese), Food(Milk)],
     [Food(Milk)],
     ....
    ]
    '''
    food_list = []
    for name in food_data.keys():
        food = Food(name, food_data[name])
        food_list.append(food)

    return list(powerset(food_list))


def split_meals_into_days(meals):

    ret = []
    counter = 1

    days_meal = []
    for meal in meals:
        if counter == 3:
            days_meal.append(meal)
            ret.append(days_meal)
            counter = 1
            days_meal = []
        else:
            counter += 1
            days_meal.append(meal)

    return ret


def find_possible_tuples(type, amount, day_meals, order=True):
    '''
    Find the possible tuple for protein
    :return:
    '''

    varDoms = []
    for v in day_meals:
        varDoms.append(v.domain())

    sat_tuples = {}
    # Find all possible sequence
    for l in itertools.product(*varDoms):
        total_amount = 0
        for foods in l:
            for food in foods:
                total_amount += food.get_amount(type)

        if total_amount <= amount:
            sat_tuples[total_amount]= l
    ret = []
    if order:
        od = collections.OrderedDict(sorted(sat_tuples.items(), reverse=True))
    else:
        od = sat_tuples

    for k, value in od.items():
        ret.append(value)
    return ret