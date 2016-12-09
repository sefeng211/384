# 384
--Project for Brent and Sean

# Overview
IMeal is a command line interface meal genearter. 

The program will ask some questions to users, and use the answers to generate some meals that meet the user requirments. 
SYSTEM REQUIREMENT： at least 4GB of memory

# Setup Constraint
After start the program, the user should answer the questions that pop up in the shell

There are 7 questions:
* Enter number of days you want to generated:
 * Users have to provide an integer
* Enter how much energy/calories do you want to have per day: 
 * Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.
* Enter how much protein do you want to have per day: 
 * Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.
* Enter how much sugar do you want to have per day:
 * Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.
* Enter how much calcium do you want to have per day: 
 * Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.
* Enter a budget limitation per day: 
 * User can answer it with an integer or leave it empty, empty response will be treated as no requirements.
* Special requests
 * There are two special requests that the user can choose. 
  * reduce repeated meals
    * If the user chooses this request, the program will try to avoid providing repeated meals to the user.
  * eat as much as you can
    * With this request, the program will try to provides the meals that meet the requirements as mush as it can. Without this request, the program will generate meals arbitrary. 
    
The program will generate constraints based on the user requirments. 

# Some new implementation
We implemented a new CSP model called MealCSP, it inherits the CSP class from assignment 2. We implemented some new helper functions in this class to improve the performance on our program.

We implemented a food class which represents a food. 

We implementated a new BT class for us to get the status of a search easily.

We also implemented a new value ordering function. This function basically handles the two special requests.


# Usage
Run main.pyf
## Example Usage and Output
```
Thanks for using IMeal
Enter number of days you want to generated: 10
Enter how much energy/calories do you want to have per day: 3000
Enter how much protein do you want to have per day: 300
Enter how much sugar do you want to have per day: 300
Enter how much calcium do you want to have per day: 2000
Enter a budget limitation per day: 1000
You can select some special request: 
Do you want to reduce repeated meals
yes
Do you want to eat as much as you can
yes
Start generating meals
CSP IMeal_model solved. CPU Time used = 0.0
CSP IMeal_model  Assignments = 
Var--Meal_0  =  (<cspbaseMeal.Food object at 0x03294810>, <cspbaseMeal.Food object at 0x03294890>, <cspbaseMeal.Food object at 0x03294830>, <cspbaseMeal.Food object at 0x0334FFD0>, <cspbaseMeal.Food object at 0x0334FF50>)     Var--Meal_1  =  (<cspbaseMeal.Food object at 0x0336B470>, <cspbaseMeal.Food object at 0x0336B490>, <cspbaseMeal.Food object at 0x0336B4B0>, <cspbaseMeal.Food object at 0x0336B4D0>)     Var--Meal_2  =  (<cspbaseMeal.Food object at 0x0336B5D0>, <cspbaseMeal.Food object at 0x0336B650>)     Var--Meal_3  =  (<cspbaseMeal.Food object at 0x0336B770>, <cspbaseMeal.Food object at 0x0336B790>, <cspbaseMeal.Food object at 0x0336B7B0>, <cspbaseMeal.Food object at 0x0336B830>)     Var--Meal_4  =  (<cspbaseMeal.Food object at 0x0336B910>, <cspbaseMeal.Food object at 0x0336B930>, <cspbaseMeal.Food object at 0x0336B950>)     Var--Meal_5  =  (<cspbaseMeal.Food object at 0x0336BA90>, <cspbaseMeal.Food object at 0x0336BAF0>, <cspbaseMeal.Food object at 0x0336BB10>)     Var--Meal_6  =  (<cspbaseMeal.Food object at 0x0336BC30>, <cspbaseMeal.Food object at 0x0336BC50>, <cspbaseMeal.Food object at 0x0336BC90>)     Var--Meal_7  =  (<cspbaseMeal.Food object at 0x0336BDB0>, <cspbaseMeal.Food object at 0x0336BDD0>)     Var--Meal_8  =  (<cspbaseMeal.Food object at 0x0336BF10>, <cspbaseMeal.Food object at 0x0336BF30>)     Var--Meal_9  =  (<cspbaseMeal.Food object at 0x035A40B0>, <cspbaseMeal.Food object at 0x035A40F0>, <cspbaseMeal.Food object at 0x035A4110>, <cspbaseMeal.Food object at 0x035A4130>)     Var--Meal_10  =  (<cspbaseMeal.Food object at 0x035A4230>, <cspbaseMeal.Food object at 0x035A4250>, <cspbaseMeal.Food object at 0x035A4290>)     Var--Meal_11  =  (<cspbaseMeal.Food object at 0x035A43B0>, <cspbaseMeal.Food object at 0x035A43D0>, <cspbaseMeal.Food object at 0x035A4430>)     Var--Meal_12  =  (<cspbaseMeal.Food object at 0x035A4550>, <cspbaseMeal.Food object at 0x035A4590>, <cspbaseMeal.Food object at 0x035A45B0>)     Var--Meal_13  =  (<cspbaseMeal.Food object at 0x035A46B0>, <cspbaseMeal.Food object at 0x035A46F0>, <cspbaseMeal.Food object at 0x035A4710>)     Var--Meal_14  =  (<cspbaseMeal.Food object at 0x035A4830>, <cspbaseMeal.Food object at 0x035A4870>, <cspbaseMeal.Food object at 0x035A48B0>)     Var--Meal_15  =  (<cspbaseMeal.Food object at 0x035A49B0>, <cspbaseMeal.Food object at 0x035A49D0>)     Var--Meal_16  =  (<cspbaseMeal.Food object at 0x035A4B70>, <cspbaseMeal.Food object at 0x035A4B90>, <cspbaseMeal.Food object at 0x035A4BB0>)     Var--Meal_17  =  (<cspbaseMeal.Food object at 0x035A4CD0>, <cspbaseMeal.Food object at 0x035A4D10>)     Var--Meal_18  =  (<cspbaseMeal.Food object at 0x035A4E50>, <cspbaseMeal.Food object at 0x035A4EB0>)     Var--Meal_19  =  (<cspbaseMeal.Food object at 0x035A4FB0>, <cspbaseMeal.Food object at 0x035A4FF0>)     Var--Meal_20  =  (<cspbaseMeal.Food object at 0x035A9190>, <cspbaseMeal.Food object at 0x035A91B0>)     Var--Meal_21  =  (<cspbaseMeal.Food object at 0x035A9310>, <cspbaseMeal.Food object at 0x035A9350>)     Var--Meal_22  =  (<cspbaseMeal.Food object at 0x035A9470>,)     Var--Meal_23  =  (<cspbaseMeal.Food object at 0x035A9610>,)     Var--Meal_24  =  (<cspbaseMeal.Food object at 0x035A9750>, <cspbaseMeal.Food object at 0x035A97B0>, <cspbaseMeal.Food object at 0x035A97D0>)     Var--Meal_25  =  (<cspbaseMeal.Food object at 0x035A98D0>, <cspbaseMeal.Food object at 0x035A9930>)     Var--Meal_26  =  (<cspbaseMeal.Food object at 0x035A9A50>, <cspbaseMeal.Food object at 0x035A9AD0>)     Var--Meal_27  =  (<cspbaseMeal.Food object at 0x035A9C30>, <cspbaseMeal.Food object at 0x035A9C50>)     Var--Meal_28  =  (<cspbaseMeal.Food object at 0x035A9D50>,)     Var--Meal_29  =  (<cspbaseMeal.Food object at 0x035A9F30>,)     
bt_search finished
Search made 80 variable assignments and pruned 0 variable values
==============Day 1 =============
Meal 1
SOUR DRSNG 
CHEESE
BUTTER
EGGNOG
MILK
Meal 2
SOUR DRSNG 
CHEESE
BUTTER
EGGNOG
Meal 3
SOUR DRSNG 
MILK
Total amount of protein is 70.01
Total amount of sugar is 31.259999999999998
Total amount of calcium is 1959.0
Total amount of price is 45.60000000000001
Total amount of energy is 2976.0
==============Day 2 =============
Meal 1
CHEESE
BUTTER
EGGNOG
MILK
Meal 2
SOUR DRSNG 
CHEESE
BUTTER
Meal 3
SOUR DRSNG 
EGGNOG
MILK
Total amount of protein is 66.76
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1846.0
Total amount of price is 45.18000000000001
Total amount of energy is 2798.0
==============Day 3 =============
Meal 1
CHEESE
BUTTER
MILK
Meal 2
CHEESE
BUTTER
Meal 3
SOUR DRSNG 
CHEESE
Total amount of protein is 72.47999999999999
Total amount of sugar is 6.3
Total amount of calcium is 1873.0
Total amount of price is 38.52
Total amount of energy is 2734.0
==============Day 4 =============
Meal 1
SOUR DRSNG 
BUTTER
EGGNOG
MILK
Meal 2
SOUR DRSNG 
CHEESE
EGGNOG
Meal 3
SOUR DRSNG 
CHEESE
MILK
Total amount of protein is 69.15999999999998
Total amount of sugar is 31.2
Total amount of calcium is 1935.0
Total amount of price is 41.97
Total amount of energy is 2259.0
==============Day 5 =============
Meal 1
CHEESE
EGGNOG
MILK
Meal 2
SOUR DRSNG 
BUTTER
EGGNOG
Meal 3
SOUR DRSNG 
BUTTER
MILK
Total amount of protein is 45.36
Total amount of sugar is 26.080000000000002
Total amount of calcium is 1318.0
Total amount of price is 35.60000000000001
Total amount of energy is 2445.0
==============Day 6 =============
Meal 1
SOUR DRSNG 
CHEESE
Meal 2
BUTTER
EGGNOG
MILK
Meal 3
CHEESE
EGGNOG
Total amount of protein is 59.33
Total amount of sugar is 21.84
Total amount of calcium is 1581.0
Total amount of price is 39.03
Total amount of energy is 1840.0
==============Day 7 =============
Meal 1
CHEESE
MILK
Meal 2
SOUR DRSNG 
BUTTER
Meal 3
BUTTER
EGGNOG
Total amount of protein is 34.23
Total amount of sugar is 13.35
Total amount of calcium is 947.0
Total amount of price is 26.22
Total amount of energy is 2116.0
==============Day 8 =============
Meal 1
BUTTER
MILK
Meal 2
CHEESE
Meal 3
BUTTER
Total amount of protein is 26.43
Total amount of sugar is 0.6200000000000001
Total amount of calcium is 704.0
Total amount of price is 18.94
Total amount of energy is 1850.0
==============Day 9 =============
Meal 1
SOUR DRSNG 
EGGNOG
MILK
Meal 2
SOUR DRSNG 
EGGNOG
Meal 3
SOUR DRSNG 
MILK
Total amount of protein is 25.509999999999998
Total amount of sugar is 30.14
Total amount of calcium is 855.0
Total amount of price is 19.180000000000003
Total amount of energy is 836.0
==============Day 10 =============
Meal 1
EGGNOG
MILK
Meal 2
SOUR DRSNG 
Meal 3
EGGNOG
Total amount of protein is 15.68
Total amount of sugar is 20.78
Total amount of calcium is 501.0
Total amount of price is 16.240000000000002
Total amount of energy is 417.0

```

