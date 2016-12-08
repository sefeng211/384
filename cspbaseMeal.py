from cspbase import Variable, CSP, BT
import time


class MealPlanVariable(Variable):
    '''
    This is the variable class for meal plan, it inherits the Variable class
     from A2.
    '''
    pass


class MealCSP(CSP):

    def __init__(self, name, reduce_repeat, vars=[]):
        '''create a CSP object. Specify a name (a string) and
           optionally a set of variables'''

        self.name = name
        self.vars = []
        self.cons = []
        self.vars_to_cons = dict()
        for v in vars:
            self.add_var(v)
        self.reduce_repeat = reduce_repeat
        self.reduce_repeat_counter = 0

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

    def is_reduce_repeat(self):
        '''
        Check if the user wants to reduce repeated meals
        :return: True if the user wants to reduce repeated meals, False
        otherwise
        '''
        return self.reduce_repeat

    def get_reduce_repeat_counter(self):
        '''
        Get the reduce repeat counter
        :return: the value of reduce_repeat_counter
        '''
        return self.reduce_repeat_counter

    def increase_reduce_repeat_counter(self):
        '''
        Increase the reduce repeat counter
        :return: None
        '''
        self.reduce_repeat_counter += 1


class Food:
    '''
    This class represents a food
    '''
    def __init__(self, food_name, nutrition_data):
        self.name = food_name
        self.nutrition_data = nutrition_data

    def get_name(self):
        '''
        Get the name of the food
        :return: the name of the food
        '''
        return self.name

    def get_nutrition_data(self):
        '''
        Get the nutrition of this food
        :return: the nutrition of this food
        '''
        return self.nutrition_data

    def get_amount(self, type):
        '''
        :return: Get how much protein does this Food has
        '''

        if type in self.nutrition_data:

            return self.nutrition_data[type]

        return 0

class MealBT(BT):

    def __init__(self, csp):
        '''csp == CSP object specifying the CSP to be solved'''

        self.csp = csp
        self.nDecisions = 0  # nDecisions is the number of variable
        # assignments made during search
        self.nPrunings = 0  # nPrunings is the number of value prunings during search
        unasgn_vars = list()  # used to track unassigned variables
        self.TRACE = False
        self.runtime = 0
        self.return_status = False

    def bt_search(self, propagator, var_ord, val_ord):
        '''
        Same as the bt search function in BT, the only difference is this
        function updates the return_status variable
        '''

        self.clear_stats()
        stime = time.process_time()

        self.restore_all_variable_domains()

        self.unasgn_vars = []
        for v in self.csp.vars:
            if not v.is_assigned():
                self.unasgn_vars.append(v)

        status, prunings = propagator(
            self.csp)  # initial propagate no assigned variables.
        self.nPrunings = self.nPrunings + len(prunings)

        if self.TRACE:
            print(len(self.unasgn_vars),
                  " unassigned variables at start of search")
            print("Root Prunings: ", prunings)

        if status == False:
            print("CSP{} detected contradiction at root".format(
                self.csp.name))
        else:
            status = self.bt_recurse(propagator, var_ord, val_ord,
                                     1)  # now do recursive search

        self.restoreValues(prunings)
        if status == False:
            print("CSP{} unsolved. Has no solutions".format(self.csp.name))
        if status == True:
            print("CSP {} solved. CPU Time used = {}".format(self.csp.name,
                                                             time.process_time() - stime))
            self.csp.print_soln()

        print("bt_search finished")
        self.print_stats()
        self.return_status = status

    def get_status(self):

        return self.return_status