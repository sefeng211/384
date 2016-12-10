=================================================
384 Project
--By Brent and Sean
=================================================

1) Overview

IMeal is a command line interface meals genearter. 

The program will ask some questions to users, and use the answers to 
generate some meals that meet the user requirments. 

2) SYSTEM REQUIREMENT
- Python 3

- At least 4GB of memory

3) Command Line User Interface
After start the program, the user should answer the questions that pop up in the shell

There are 7 questions:
1. Enter number of days you want to generated:
--- Users have to provide an integer

2. Enter how much energy/calories do you want to have per day: 
--- Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.

3. Enter how much protein do you want to have per day: 
--- Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.

4. Enter how much sugar do you want to have per day:
--- Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.

5. Enter how much calcium do you want to have per day: 
--- Users can answer it with an integer or leave it empty, empty response will be treated as no requirements.

6. Enter a budget limitation per day: 
--- User can answer it with an integer or leave it empty, empty response will be treated as no requirements.

7. Special requests
   1) There are two special requests that the user can choose. 
	---- reduce repeated meals
    2) If the user chooses this request, the program will try to avoid providing repeated meals to the user.
    ---- eat as much as you can
    With this request, the program will try to provides the meals that meet the requirements as mush as it can. Without this request, the program will generate meals arbitrary. 
    
The program will generate constraints based on the user requirments.


4) Usage
command: python3 main.py

Please Note that if answer to the question "Do you want to eat as much as you can" is "yes", use food_nutrition_small_13.csv
Otherwise can use food_nutrition_small_13.csv or food_nutrition_big_28.csv

In order to change the database file, please edit the constant string DATA_FILE in main.py.
It sets to 'food_nutrition_small_13.csv' by default.


```
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
Gerneate CSP Model takes 0.1096200942993164
CSP IMeal_model solved. CPU Time used = 0.015625
CSP IMeal_model  Assignments = 
Var--Meal_0  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_1  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_2  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_3  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_4  =  (<cspbaseMeal.Food object at 0x034B8050>,)     Var--Meal_5  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_6  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_7  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_8  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_9  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_10  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_11  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_12  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_13  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_14  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_15  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_16  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_17  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_18  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_19  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_20  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_21  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_22  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_23  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_24  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_25  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_26  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     Var--Meal_27  =  (<cspbaseMeal.Food object at 0x034B8070>, <cspbaseMeal.Food object at 0x034B8090>, <cspbaseMeal.Food object at 0x034B80B0>, <cspbaseMeal.Food object at 0x034B80D0>)     Var--Meal_28  =  (<cspbaseMeal.Food object at 0x034B8050>, <cspbaseMeal.Food object at 0x034B8110>)     Var--Meal_29  =  (<cspbaseMeal.Food object at 0x034B80F0>, <cspbaseMeal.Food object at 0x034B8190>, <cspbaseMeal.Food object at 0x034B81B0>)     
bt_search finished
Search made 30 variable assignments and pruned 0 variable values
============== Day 1 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 2 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 58.879999999999995
Total amount of sugar is 18.53
Total amount of calcium is 1588.0
Total amount of price is 38.36
Total amount of energy is 2647.0
============== Day 3 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 4 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 5 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 6 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 7 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 8 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 9 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
============== Day 10 =============
============== Meal 1 =============
BUTTER
SOUR DRSNG 
BUTTER_2
SOUR DRSNG _2
============== Meal 2 =============
EGGNOG
EGGNOG_2
============== Meal 3 =============
CHEESE
MILK
CHEESE_2
Total amount of protein is 63.43
Total amount of sugar is 26.580000000000002
Total amount of calcium is 1718.0
Total amount of price is 42.71
Total amount of energy is 2735.0
```

