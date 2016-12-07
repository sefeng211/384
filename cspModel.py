from cspbase import *
'''
Construct and return CSP model for IMeal.
'''

def IMeal_Model(user_input_dic):
    '''
    Construct and return CSP model for IMeal.
    :param user_input_dic: A dictionary that contains all user input information
    :return: return a CSP Model for IMeal
    '''

    csp = CSP('IMeal_model', [])
    num_meals = user_input_dic['num_meals']

    # Each meal plan will be variable
    for i in range(0, num_meals):
        variable_name = 'Meal_'+ str(i)
        # The domain of each varialbe will be the food selection
        var_domain = None
        var = Variable(variable_name, var_domain)
        csp.add_var(var)


def create_domain(food_data):
    '''
    create the domain for variables based on the input food data
    :param food_data: The possible food selection
    Assume the food_data is in this format
    {
        '



    }
    :return:
    '''
    pass
