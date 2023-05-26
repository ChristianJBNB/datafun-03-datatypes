"""
Name: Christian Jackson
Date: 5/26/23
Domain: NBA Players
Project: 3 task 5

Working with tuples, sets, and dictionaries
"""

from util_datafun_logger import setup_logger
logger,logname = setup_logger(__file__)

#Introduction logging for function

logger.info("Task 5. Tuples and More")
logger.info("Working with tuples, sets, and dictionaries")
logger.info("")

tuple_home_team = (15, 22, 23, 40, 77)
tuple_away_team = (14, 15, 25, 30, 33)

logger.info(f"Tuple of home team jersey numbers {tuple_home_team = }")
logger.info(f"Tuple of away team jersey numbers {tuple_away_team = }")

#Practice with tuples

tuple_cat = tuple_home_team + tuple_away_team
logger.info(f"Here is the entire collection of jersey numbers for the two teams {tuple_cat}")

tuple_thrice = tuple_cat * 5
logger.info(f"Here is the total collection of jersey numbers multiplied by 5 {tuple_thrice}")

contains_15 = 15 in tuple_home_team
contains_16 = 16 in tuple_away_team
logger.info(f"T/F: The jersey number 15 is on the home team: {contains_15}")
logger.info(f"T/F: The jersey number 16 is on the away team: {contains_16}")

logger.info(f"The third jersey number of the home team is {tuple_home_team[2]} and the fourth number of the away team is {tuple_away_team[3]}")

def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

q, r = divide_and_remainder(tuple_home_team[-1], tuple_away_team[0])
logger.info(f"Quotient: {q}, Remainder: {r}")

#Practice with sets

players_pts_all_time_set = {"Lebron James", "Kareem Abdul-Jabbar", "Karl Malone", "Kobe Bryant", "Michael Jordan"}
players_pts_current_set = {"Lebron James", "Kevin Durant", "James Harden", "Russell Westbrook", "Chris Paul"}
logger.info(f"Here is the list of the top 5 all time leading scores in NBA history: {players_pts_all_time_set}")
logger.info(f"Here is the list of the top 5 current leading scores in NBA history: {players_pts_current_set}")

players_union = players_pts_all_time_set | players_pts_current_set
logger.info(f"Here are the two sets combined into one {players_union}")

players_intersection = players_pts_all_time_set & players_pts_current_set
logger.info(f"Here are the intersections of the two sets {players_intersection}")

#Practice with dictionaires

with open("text_woodchuck.txt") as fileObject:
    word_list = fileObject.read().split()

word_counts_dict = {word: word_list.count(word) for word in word_list}
logger.info(f"Here are the key-value pairs of each word and its count from the text_woodchuck.txt file: {word_counts_dict}")



with open(logname, 'r') as file_wrapper:
    print(file_wrapper.read())