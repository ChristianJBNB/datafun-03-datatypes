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
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())



