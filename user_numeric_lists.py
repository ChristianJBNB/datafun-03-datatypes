"""
Name: Christian Jackson
Date: 5/23/23
Domain: NBA Players
Project: 3 task 3

Create numeric lists to practice manipulating and using built in functions, methods, and transformations

"""

# import some standard modules first - how many can you make use of?

import math
import statistics

# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions

#list1: Number of points scored by an NBA team for 20 or so games

list1 = [
    114,
    122,
    133,
    98,
    100,
    107,
    129,
    114,
    111,
    94,
    88,
    106,
    117,
    140,
    131,
    119,
    145,
    118,
    127,
    154
]

#listx: First 10 games of the NBA season

listx = range(10)

#listy: Number of points scored by a NBA player in those first 10 games

listy = [20, 22, 31, 40, 18, 19, 16, 33, 35, 25]

# TODO: define some custom functions

#Task 3-1: List 1. List Statistics

def list_1_descriptive_stats():

    #Introduction logging for function

    logger.info("List 1. List Statistics")
    logger.info("Calculating important statistics for the number of points scored by an NBA team")
    logger.info("")
    logger.info(f"This is the list of scores for an NBA team for 20 games: {list1}")
    
    #Calculation of Mean, Median, Mode

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    #Logging of information

    logger.info(f"The mean for number of points scored for 20 games by an NBA team is: {mean:.2f}")
    logger.info(f"The median for number of points scored for 20 games by an NBA team is: {median:.2f}")
    logger.info(f"The mode for number of points scored for 20 games by an NBA team is: {mode:.2f}")

    #Calculation of standard deviation and variance

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    #Logging of information

    logger.info(f"The standard deviation for number of points scored for 20 games by an NBA team is: {stdev:.2f}")
    logger.info(f"The variance for number of points scored for 20 games by an NBA team is: {variance:.2f}")
    logger.info("")


#Task 3-2: List 2. Lists - Correlation and Prediction

def list_2_correlation_prediction():
    
    #Introduction logging for function

    logger.info("List 2. Lists - Correlation and Prediction")
    logger.info("Calculating correlation, slope and intercept of best fit line, and predicting y value at future x time")
    logger.info("")
    logger.info(f"In the first {listx} games of an NBA players season, he scored {listy} points")

    #Calculate correlation, slope and intercept 

    correlation = statistics.correlation(listx, listy)
    slope, intercept = statistics.linear_regression(listx, listy)

    #Logging of information

    logger.info(f"The correlation between the first 10 games played by an NBA player and the number of points scored in said games is {correlation:.2f}")
    logger.info(f"The slope, number of game, is {slope:.2f}")
    logger.info(f"The intercept, number of points scored, is {intercept:.2f}")

    #Future Time = 15, Predict y value

    future_time = 15
    predictiony = slope * future_time + intercept

    #Logging of information

    logger.info(f"In game {future_time}, we predict that the NBA Player will score {predictiony} points")
    logger.info("")

#Task 3-3: Lists 3. Lists - Using Python Built-in Functions 

def list_3_built_in_functions():

    #Introduction logging for function

    logger.info("Lists 3. Lists - Using Python Built-in Functions ")
    logger.info("Calculating statistics using built-in functions")
    logger.info("")

    #Using built-in functions

    minimum = min(list1)
    maximum = max(list1)
    length = len(list1)
    sum1 = sum(list1)
    average = sum1 / length
    set1 = set(list1)
    sorted1 = sorted(list1)
    sorted2 = sorted(list1, reverse=True)

    #Logging of the information
    
    logger.info(f"The minimum number of points scored by an NBA team is {minimum}")
    logger.info(f"The maximum number of points scored by an NBA team is {maximum}")
    logger.info(f"The number of NBA Games played was {length}")
    logger.info(f"The sum of all the points from the games played by an NBA team is {sum1}")
    logger.info(f"The average number of points scored in a game by a NBA team is {average:.2f}")
    logger.info(f"The number of points scored, without any repeats, by an NBA team are {set1}")
    logger.info(f"The number of points scored by an NBA team sorted from smallest to largest is {sorted1}")
    logger.info(f"The number of points scored by an NBA team sorted from largest to smallest is {sorted2}")
    logger.info("")

#Task 3-4: Lists 4. List Methods

def list_4_list_methods():

    #Introduction logging for function

    logger.info("Lists 4. List Methods")
    logger.info("Using list methods to make alterations to a list")
    logger.info("")

    #Using list methods, lst represnts jersey numbers of players in the starting lineup of an NBA team as well as logging data

    lst = [2, 9, 11, 13, 43]

    logger.info(f"Here are the inital jersey numbers of NBA players in the starting lineup {lst}")

    lst.append(5)
    logger.info(f"Appending a new jersey to the list of jeresy numbers {lst}")

    lst.extend([17, 13, 23, 44, 55])
    logger.info(f"Adding the opposing teams jersey numbers {lst}")

    lst.insert(2, 16)
    logger.info(f"Adding a new jersey number to the original team in the third slot {lst}")

    lst.remove(5)
    logger.info(f"Removing the jersey number 5 from the team {lst}")

    count_list = lst.count(2)
    logger.info(f"Counting the number of times jersey number 2 appears {count_list}")

    lst.sort()
    logger.info(f"Sorting the list into order from smallest to largest {lst}")

    lst.sort(reverse=True)
    logger.info(f"Sorting the list into order from largest to smallest {lst}")

    copy_list = lst.copy()
    copy_list.remove(44)
    logger.info(f"It would appear that a member of the team has left {copy_list}")
    logger.info(f"Here is the original list before that happened {lst}")

    lst.pop(0)
    logger.info(f"The first jersey number on the team has left {lst}")

    lst.pop(-1)
    logger.info(f"The last jersey number on the team has left {lst}")
    logger.info("")

#Task 3-5: Lists 5. List Transformations - Using filter() and map()

def list_5_list_transformations():

    #Introduction logging for function

    logger.info("Lists 5. List Transformations - Using filter() and map()")
    logger.info("Using the filter() and map() methods to transform the list")
    logger.info("")

    #List being used for transformations

    lst = [2, 19, 25, 13, 43]

    #Keep x such that x is less than 4 

    jersey_num_over_20 = list(filter(lambda x : x > 20, lst))
    logger.info(f"Here are all of the jersey numbers over 20 {jersey_num_over_20}")

    #Map each x to cuberoot of x 

    cubed_root_jersey_nums = list(map(lambda x : math.cbrt(x), lst))
    logger.info(f"Here are the cube roots of the jersey numbers {cubed_root_jersey_nums}")

    #Calculate the volume of a cube with a side equal to the value in your list

    volume_of_cubes = list(map(lambda x : x * x * x, lst))
    logger.info(f"Here are the calculations of the volume of a cube using the jersey numbers {volume_of_cubes}")
    logger.info("")

#Task 3-6: Lists 6. List Transformations - Using List Comprehension

def list_6_list_transformations_comprehension():

    #Introduction logging for function

    logger.info("Lists 6. List Transformations - Using List Comprehension")
    logger.info("Using list comprehensions to transform data")
    logger.info("")

    #Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) if x is less than 4 or some other cutoff. 

    num_of_pts_under_105 = [x for x in list1 if x < 105]
    logger.info(f"Here is the collection of games where an NBA team scored less than 105 points {num_of_pts_under_105}")

    #Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 

    triple_num_of_pts = [x*3 for x in list1]
    logger.info(f"Here is the collection of number of points scored in a game multipled by 3 {triple_num_of_pts}")

    #Use a list comprehension to transform your numeric list into another numeric list using a transformation of your choice.

    removing_uneven_scores = [x for x in list1 if x % 2 == 0]
    logger.info(f"Here are the collection of games where an NBA team scored an even number of points {removing_uneven_scores}")







# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    list_1_descriptive_stats()
    list_2_correlation_prediction()
    list_3_built_in_functions()
    list_4_list_methods()
    list_5_list_transformations()
    list_6_list_transformations_comprehension()
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())



