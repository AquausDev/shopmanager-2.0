import os, sys, time

class VariableHandling():
    def init_varibles():
        global username
        username = input("What is your name? ")

class GeneralFunctions():
    def start_up():
        start = input("Welcome to Shop Manager. What would you like to do out of the following:\n 1. Start a Game\n 2. Load a Game\n 3. Exit Game\n> ")
        
        if start.lower() in ["1", "start", "start a game"]:
            print("Starting Game...\n")
            GameManagement.run_game()
            
        elif start.lower() in ["2", "load", "load a game"]:
            print("Loading Game...\n")
            DataHandling.load_data()
            
        elif start.lower() in ["3", "quit", "exit", "exit game", "quit game"]:
            print("Quitting...")
            DataHandling.handle_exit()
            
    def handle_file_loc():
        cwd = os.getcwd()
        cwd += "\Data"
        return cwd
        
class GameManagement():
    def run_game():
        VariableHandling.init_varibles()
        DataHandling.save_data()

class DataHandling():
    def handle_exit():
        game_quit = input("Would you like to quit? ")
        #TODO: replace temp. list with yes_list/no_list variable
        if game_quit in["yes", "y"]:
            game_quit2 = input("Are you sure? ")
            if game_quit2 in["yes", "y"]:
                DataHandling.autosave_data()
                sys.exit
                
    def data_to_save(filename):
        global username
        filename.write(username)
        
    def save_data():
        ask_sav = input("Would you like to save your game? ")
        #TODO: replace temp. list with yes_list/no_list variable
        if ask_sav.lower() in ["yes", "y"]:
            save_cwd = GeneralFunctions.handle_file_loc() + "\Saves\ " + username.lower() + "_sav.sav"
            file = open(save_cwd, "w")
            DataHandling.data_to_save(file)
            file.close()
            print("Game saved.")
        else:
            print("Game not saved.")

    def autosave_data():
        save_cwd = GeneralFunctions.handle_file_loc() + "\Saves\ " + username.lower() + "_auto.sav"
        file = open(save_cwd, "w")
        DataHandling.data_to_save(file)
        file.close()
        
    def load_data():
        username = input("What is the save name? ")
        load_cwd = GeneralFunctions.handle_file_loc() + "\Saves\ " + username.lower() + ".sav"
        file = open(load_cwd, "r")
        #TODO: add data to load, temp. code below
        for line in file:
            print(line)
        file.close()
        
GeneralFunctions.start_up()
