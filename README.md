# 384
--Project for Brent and Sean

# Overview
IMeal is a command line interface meal genearter. 

The program will ask some questions to users, and use the answers to generate some meals that meet the user requirments. 

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
# Usage
Step 1: Run main.pyf
-- After running main.py, the user should answer the questions that pops up in the shell.
There are 6 questions
2) df
3)
