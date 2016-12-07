from cspbase import Variable, CSP

class MealPlanVariable(Variable):
    '''
    This is the variable class for meal plan, it inherits the Variable class
     from A2.
    '''

    # TODO: Add appropriate functions or overwrite some parent class functions


    pass

class MealCSP(CSP):

    def add_var(self, v):
        '''Add variable object to CSP while setting up an index
           to obtain the constraints over this variable'''
        if not type(v) is MealPlanVariable:
            print("Trying to add non meal plan variable ", v, " to CSP object")
        elif v in self.vars_to_cons:
            print("Trying to add variable ", v,
                  " to CSP object that already has it")
        else:
            self.vars.append(v)
            self.vars_to_cons[v] = []
class Food:
    '''
    This class represents a food
    '''
    def __init__(self, food_name, nutrition_data):
        self.name = food_name
        self.nutrition_data = nutrition_data

    def get_name(self):
        return self.name

    def get_nutrition_data(self):
        return self.nutrition_data

    def get_amount(self, type):
        '''
        :return: Get how much protein does this Food has
        '''

        if type in self.nutrition_data:

            return self.nutrition_data[type]

        return 0

