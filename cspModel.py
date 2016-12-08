from cspbase import *
from cspbaseMeal import *
from orderings import *
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
BUDGET = 'price'
MEALS = 'meals'


def IMeal_Model(user_input_dic, food_data):
    '''
    Construct and return CSP model for IMeal.
    :param user_input_dic: A dictionary that contains all user input information
    :return: return a CSP Model for IMeal
    '''

    csp = MealCSP('IMeal_model', [])
    num_meals = user_input_dic[MEALS]
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
    meals_in_total = csp.get_all_vars()

    c = Constraint("Protein_Cons",
                   meals_in_total)
    all_possible_tuples = find_possible_tuples(PROTEIN, protein, meals_in_total)
    c.add_satisfying_tuples(all_possible_tuples)
    csp.add_constraint(c)

    # Sugar Constraint
    c = Constraint("Sugar_Cons",
                   meals_in_total)
    all_possible_tuples = find_possible_tuples(SUGAR, sugar, meals_in_total)
    c.add_satisfying_tuples(all_possible_tuples)
    csp.add_constraint(c)

    # Calcium Constraint
    c = Constraint("Calcium_Cons",
                   meals_in_total)
    all_possible_tuples = find_possible_tuples(CALCIUM, calcium, meals_in_total)
    c.add_satisfying_tuples(all_possible_tuples)
    csp.add_constraint(c)

    # Budget Constraint
    c = Constraint("Budget_Cons",
                   meals_in_total)
    all_possible_tuples = find_possible_tuples(BUDGET, budget, meals_in_total)
    c.add_satisfying_tuples(all_possible_tuples)
    csp.add_constraint(c)

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
    :return: All possible tuples
    '''

    varDoms = []
    for v in day_meals:
        varDoms.append(v.domain())

    sat_tuples = defaultdict(list)
    # Find all possible sequence
    sequence = itertools.product(*varDoms)
    for l in sequence:
        total_amount = 0

        for foods in l:
            for food in foods:
                total_amount += food.get_amount(type)

        if total_amount <= amount:
            sat_tuples[total_amount].append(l)

    ret = []
    if order:
        od = collections.OrderedDict(sorted(sat_tuples.items(), reverse=True))
    else:
        od = sat_tuples

    for k, value in od.items():
        for v in value:
            ret.append(v)

    return ret