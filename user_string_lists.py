"""
Name: Christian Jackson
Date: 5/25/23
Domain: NBA Players
Project: 3 task 4

Working with string lists to transform data
"""

# imports first

import random

from util_datafun_logger import setup_logger
logger, logname = setup_logger(__file__)

#The string lists I will be using

nba_teams = ["Mavricks", "Pelicans", "Lakers", "Celtics", "Bulls"]
nba_players = ["Luka Doncic", "Zion Williamson", "Lebron James", "Jayson Tatum", "Zach Lavine"]
nba_arenas = ["American Airlines Center", "Smoothie King Center", "Crypto.com Arena", "TD Garden", "United Center"]
nba_legends = ["Dirk Nowitzki", "Pistol Pete", "Kareen Abdul-Jabbar", "Bill Russell", "Scottie Pippen"]
nba_owners = ["Mark Cuban", "Gayle Benson", "Jeanie Buss", "Wyc Grousbeck", "Jerry Reinsdorf"]

# reusable functions next

def string_lists_task_4():
    
    #Introduction logging for function

    logger.info("String Lists 1. Using Python Built-in Functions ")
    logger.info("Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.")
    logger.info("")

    #Getting len of all of the lists

    len_nba_teams = len(nba_teams)
    len_nba_players = len(nba_players)
    len_nba_areans = len(nba_arenas)
    len_nba_legends = len(nba_legends)
    len_nba_owners = len(nba_owners)
    logger.info(f"Here are the lenghts of all of the lists I have created. NBA teams: {len_nba_teams}, NBA Players: {len_nba_players}, NBA Arenas: {len_nba_areans}, NBA Legends: {len_nba_legends}, NBA Owners: {len_nba_owners}")

    #Converting every list into a set

    set_nba_teams = set(nba_teams)
    set_nba_players = set(nba_players)
    set_nba_areans = set(nba_arenas)
    set_nba_legends = set(nba_legends)
    set_nba_owners = set(nba_owners)
    logger.info(f"Here are the sets of all of the lists I have created. NBA teams: {set_nba_teams}, NBA Players: {set_nba_players}, NBA Arenas: {set_nba_areans}, NBA Legends: {set_nba_legends}, NBA Owners: {set_nba_owners}")

    #Zipping two lists into a tuple

    zip_of_lists = zip(nba_players, nba_legends)
    logger.info(f"Here is a tuple of two combined lists {tuple(zip_of_lists)}")
    logger.info("")


def string_lists_task_4_p2():
    
    #String Lists 2. Random Choice

    logger.info("String Lists 2. Random Choice")
    logger.info("Using random to get a random team, player, arean, legend, and owner.")
    logger.info("")

    #Random sentence generator using random.choice and lists

    sentence_generator = (f"We are going to create a new franchise using existing ones. First, the team name is the {random.choice(nba_teams)}. "
    f"Next we are getting the main player for the team, and that person is {random.choice(nba_players)}. We also need an arena, which will be {random.choice(nba_arenas)}. "
    f"Next is the legend that once played for the team, and that is {random.choice(nba_legends)}. Finally is the owner of the team, {random.choice(nba_owners)}. "
    "Congratuations on your new NBA franchise.")
    logger.info(f"Here is your new franchise: {sentence_generator}")

def string_lists_task_4_p3():
    
    #String Lists 3. Get Unique Words

    logger.info("String Lists 3. Get Unique Words")
    logger.info("Reading in a text file and using built-in functions to analyze it")
    logger.info("")

    #Reading in text_hamlet.txt and splitting all of the words up, then making sure to get rid of the duplicates using set()

    with open("text_hamlet.txt", "r") as fileObject:
        text = fileObject.read()
        all_words = text.split()
        unique_words = set(all_words) 
        sorted_unique_words = sorted(unique_words)

        logger.info(f"Here is the length of all the words from text_hamlet.txt: {len(all_words)}")
        logger.info(f"Here is the length of all the unqiue words from from text_hamlet.txt: {len(unique_words)}")
        logger.info(f"Here is the length of all the unique words from from text_hamlet.txt sorted: {sorted_unique_words}")
        
# call functions and execute code

if __name__ == "__main__":
    string_lists_task_4()
    string_lists_task_4_p2()
    string_lists_task_4_p3()
    with open(logname, 'r') as file_wrapper:
        print(file_wrapper.read())
