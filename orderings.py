#Look for #IMPLEMENT tags in this file. These tags indicate what has
#to be implemented.

import random
import collections
from collections import defaultdict
'''
This file will contain different variable ordering heuristics to be used within
bt_search.

var_ordering == a function with the following template
    ord_type(csp)
        ==> returns Variable 

    csp is a CSP object---the heuristic can use this to get access to the
    variables and constraints of the problem. The assigned variables can be
    accessed via methods, the values assigned can also be accessed.

    ord_type returns the next Variable to be assigned, as per the definition
    of the heuristic it implements.

val_ordering == a function with the following template
    val_ordering(csp,var)
        ==> returns [Value, Value, Value...]
    
    csp is a CSP object, var is a Variable object; the heuristic can use csp to access the constraints of the problem, and use var to access var's potential values. 

    val_ordering returns a list of all var's potential values, ordered from best value choice to worst value choice according to the heuristic.

'''


class Dictlist(dict):
    def __setitem__(self, key, value):
        try:
            self[key]
        except KeyError:
            super(Dictlist, self).__setitem__(key, [])
        self[key].append(value)

def ord_random(csp):
    '''
    ord_random(csp):
    A var_ordering function that takes a CSP object csp and returns a Variable object var at random.  var must be an unassigned variable.
    '''
    var = random.choice(csp.get_all_unasgn_vars())
    return var


def val_arbitrary(csp,var):
    '''
    val_arbitrary(csp,var):
    A val_ordering function that takes CSP object csp and Variable object var,
    and returns a value in var's current domain arbitrarily.
    '''
    return var.cur_domain()


def ord_mrv(csp):
    '''
    ord_mrv(csp):
    A var_ordering function that takes CSP object csp and returns Variable object var, 
    according to the Minimum Remaining Values (MRV) heuristic as covered in lecture.  
    MRV returns the variable with the most constrained current domain 
    (i.e., the variable with the fewest legal values).
    '''

    # IMPLEMENT
    # Our goal here is that
    # Go through each variables, and find which one has the fewest legal values
    # and return the values
    result_dic = ord_mrv_helper(csp)
    if result_dic == {}:
        # If the input cps has no un assigned variables
        return None
    else:
        # Return the key that has minimum value (fewest legal values)
        return min(result_dic, key=result_dic.get)

def ord_mrv_helper(csp):
    """
    A helper function for order_mrv that finds the current domain size for each
    variable in the input csp.
    :param csp: The model of the csp that contains all the information such as
    Contraints and variables
    :return: Returns a Ordered dictionary that the keys are the variable and the values
    are the current domain size of each value.
    """

    variables = csp.get_all_unasgn_vars()  # Find all unassgined varabiles
    ret = collections.OrderedDict()
    for var in variables:
        cur_domain_size = var.cur_domain_size() # Find the current domain size
        ret[var] = cur_domain_size # Store them in the dictionary

    return ret

def ord_dh(csp):
    '''
    ord_dh(csp):
    A var_ordering function that takes CSP object csp and returns Variable object var,
    according to the Degree Heuristic (DH), as covered in lecture.
    Given the constraint graph for the CSP, where each variable is a node, 
    and there exists an edge from two variable nodes v1, v2 iff there exists
    at least one constraint that includes both v1 and v2,
    DH returns the variable whose node has highest degree.
    '''
    # IMPLEMENT
    # Go through each variables and find which one has the highest degree.
    result_dic = ord_dh_helper(csp)
    if result_dic == {}:
        # If the input csp has no unassigned variables
        return None
    else:
        # Return the variable that has the max value(highest degree)
        return max(result_dic, key=result_dic.get)


def ord_dh_helper(csp):
    """
    A helper function for order_dh that takes CSP object and finds the degree
    of each variables based on degree heuristic.
    :param csp: The input CSP Object.
    :return: Return a ordered dictionary that the keys are the variables and
    the value of the keys are the degree of each variables.
    """
    variables = csp.get_all_unasgn_vars()  # Find all unassgined varabiles
    ret = collections.OrderedDict()
    for var in variables:
        cons = csp.get_cons_with_var(var)
        # Find how many unassigned variables for each constraint (degree)
        num_unassign = 0
        # In case there are same variables in different cons, using the list
        # to keep track of the unassigned variables that has been counted
        added_variables = []
        for con in cons:
            for v in con.get_unasgn_vars():
                if v not in added_variables:
                    added_variables.append(v)
                    num_unassign += 1
        ret[var] = num_unassign
    return ret


def val_lcv(csp, var):
    '''
    val_lcv(csp,var):
    A val_ordering function that takes CSP object csp and Variable object var,
    and returns a list of Values [val1,val2,val3,...]
    from var's current domain, ordered from best to worst, evaluated according to the 
    Least Constraining Value (LCV) heuristic.
    (In other words, the list will go from least constraining value in the 0th index, 
    to most constraining value in the $j-1$th index, if the variable has $j$ current domain values.) 
    The best value, according to LCV, is the one that rules out the fewest domain values in other 
    variables that share at least one constraint with var.
    '''
    # IMPLEMENT
    result_dic = lcv_helper(csp, var)
    return sorted(result_dic, key=result_dic.get)

def val_odering_max(csp, var):

    current_domain = var.cur_domain()
    dic = defaultdict(list)
    for v in current_domain:
        total_protein = 0
        for food in v:
            total_protein += food.get_amount('protein')

        dic[total_protein].append(v)

    ret = []
    od = collections.OrderedDict(sorted(dic.items(), reverse=True))

    for k, value in od.items():
        for v in value:
            ret.append(v)
    return ret


def lcv_helper(csp, var):
    """
    A helper function of val_lcv that takes a CSP Object and a variable, and
    finds how many values that the variable would rules out for each variables.
    :param csp: The input CSP Object
    :param var: The input variable object
    :return: Returns a dictionary such that the keys are the values and the
    values of the dictionary are the number of values that would be ruled out.
    """
    current_domain = var.cur_domain()
    dic = {}
    for value in current_domain:
        var.assign(value) # Temporary assign the value
        counter = 0
        for con in csp.get_cons_with_var(var):  # Find the constrains of the var
            for v in con.get_unasgn_vars():
                if v != var:
                    for s in v.cur_domain():
                        if not con.has_support(v, s):
                            # This value has no support means this value will
                            # be ruled out
                            counter += 1
        # Unassign the value
        var.unassign()
        dic[value] = counter
    return dic


def ord_custom(csp):
    '''
    ord_custom(csp):
    A var_ordering function that takes CSP object csp and returns Variable object var,
    according to a Heuristic of your design.  This can be a combination of the ordering heuristics
    that you have defined above.
    '''

    # IMPLEMENT
    # My algorithm is rank each variables based on the mrv result and dh result
    # and then find one which has an average best result

    dic_mrv = ord_mrv_helper(csp)
    dic_dh = ord_dh_helper(csp)
    if dic_dh == {} or dic_mrv == {}:
        return None
    # smaller index means better mrv result
    rank_mrv = sorted(dic_mrv, key=dic_mrv.get)

    # larger index means better dh result
    rank_dh = sorted(dic_dh, key=dic_dh.get)
    total_rank = collections.OrderedDict()

    for i in range(0, len(rank_mrv)):
        total_rank[rank_mrv[i]] = i

    for i in range(0, len(rank_dh)):
        total_rank[rank_dh[i]] += len(rank_dh) - i

    return sorted(total_rank, key=total_rank.get)[0]
