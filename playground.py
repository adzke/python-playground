
import time
import random
import pickle
import time 
from art import *

playstatus = True
level_up = "level_up"
gold_price = 200


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def blank_game_load():
    blank_game_data = {
        "experience": 0,
        "pickaxe_level": 2,
        "gold": 0,
        "cash": 0,
        "diamond": 0,
        "dragon_stone": 0
    }
    pickle.dump(blank_game_data, open("miningdata.pkl", "wb"))


def load_game_data():
    #blank_game_load()
    loaded_data = pickle.load(open("miningdata.pkl", "rb"))

    if(bool(loaded_data)):
        print(loaded_data)
        return loaded_data

    else:
        print("no game data")
        blank_game_data = {"experience": 0, "pickaxe_level": 2}
        pickle.dump(blank_game_data, open("miningdata.pkl", "wb"))
        return blank_game_data


def save_game_data(game_data):
    pickle.dump(game_data, open("miningdata.pkl", "wb"))


miningdata = load_game_data()


def generate_random_time():
    return random.uniform(0.2, 2.0)


def game_section(status):
    match status:
        case "level_up":
            return level_up


def sell_gold():
    cash_back = miningdata["gold"] * gold_price
    print(cash_back)
    miningdata["gold"] = 0
    miningdata["cash"] = cash_back


def generate_experience():
    random_range = random.uniform(1.0, 3.5)
    experience_calculator = random_range * miningdata["pickaxe_level"]
    return round(experience_calculator, 2)


def find_gold():
    random_range = round(random.uniform(1, 10), 0)
    if(random_range == 10):
        print(bcolors.OKBLUE + "YOU FIND A GOLD NUGGET" + bcolors.ENDC)
        miningdata["gold"] += 1


def find_dimaond():
    random_range = round(random.uniform(1, 10), 0)
    if(random_range == 10):
        drop_table_range = round(random.uniform(1, 20), 0)
        print(bcolors.OKGREEN + "Good luck, rolling: " + str(int(drop_table_range)) + "/20"+ bcolors.ENDC)

        if(drop_table_range == 20):
            print(bcolors.WARNING + "VERY RARE!!!!!!! YOU FIND A DIAMOND !!!!!!!!!" + bcolors.ENDC)
            miningdata["diamond"] += 1

def find_dragon_stone():
    random_range = round(random.uniform(1, 10), 0)
    if(random_range == 1):
        drop_table_range = round(random.uniform(1, 500), 0)
        print(bcolors.OKCYAN + "Good luck, rolling for dragon stone: " + str(int(drop_table_range)) + "/500"+ bcolors.BOLD)

        if(drop_table_range == 500):
            print(bcolors.FAIL + "ULTRA RARE!!!!!!! YOU FIND A D R A G O N S T O N E !!!!!!!!!" + bcolors.ENDC)
            miningdata["dragon_stone"] += 1


while playstatus:
    print("Welcome, please enter your choice")
    print("1. Gain exp")
    print("2. Sell items")

    main_input = input()
    if(main_input == "1"):
        try:
            program_starts = time.time()
            while True:
                print(bcolors.HEADER + "mining" + bcolors.ENDC)
                
                miningdata["experience"] += generate_experience()
                find_gold()
                find_dimaond()
                find_dragon_stone()
                time.sleep(generate_random_time())
                # print(round(miningdata["experience"], 2))
        except KeyboardInterrupt:
            print("Cancelled")
            now = time.time()
            print("Spent {0} second(s) mining".format(int(now) - int(program_starts)))
            save_game_data(miningdata)

    if(main_input == "2"):
        try:
            print("Welcome to the shop, please select an option.")
            print("1. Sell gold")
            sell_menu = input()
            if(sell_menu == "1"):
                print("gold sold")
                sell_gold()

        except KeyboardInterrupt:
            print("Cancelled")
            save_game_data(miningdata)
