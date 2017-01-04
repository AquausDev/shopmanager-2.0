import os, sys, time

class VariableHandling():
    def init_varibles():
        username = input("What is your name? ")
        day = 1

        return username, day

class GeneralFunctions():
    def start_up():
        start = input("Welcome to Shop Manager. What would you like to do out of the following:\n1. Start a Game\n2. Load a Game\n3. Play Tutorial\n4. Exit Game\n")
        
        if start.lower() in ["1", "start", "start a game"]:
            print("Starting Game...\n")
            GameManagement.run_game()
            
        elif start.lower() in ["2", "load", "load a game"]:
            print("Loading Game...\n")
            
        elif start.lower() in ["3", "tutorial", "play tutorial"]:
            print("Loading Tutorial...\n")
            
        elif start.lower() in ["4", "quit", "exit", "exit game", "quit game"]:
            print("Quitting...\n")
            sys.exit
            
    def handle_file_loc():
        cwd = os.getcwd()
        cwd += "\Data"
        return cwd

    def day_management():
        print("Day " + str(day) + "\n")
        day += 1
        
class GameManagement():
    def run_game():
        VariableHandling.init_varibles()
        DataHandling.autosave_data()
        
        #while True:
        GeneralFunctions.day_management()

class DataHandling():
    def data_to_save(filename):
        filename.write(username)
        
    def save_data():
        #rechecks the current working directory
        save_cwd = GeneralFunctions.handle_file_loc() + "\Saves\ "+ username.lower() + ".sav"
        file = open(save_cwd, "w")
        #data store
        DataHandling.data_to_save(file)
        file.close()

    def autosave_data():
        #rechecks the current working directory
        save_cwd = GeneralFunctions.handle_file_loc() + "\Saves\ "+ username.lower() + "_autosave.sav"
        file = open(save_cwd, "w")
        #data store
        DataHandling.data_to_save(file)
        file.close()
        
    def load_data():
        #rechecks the current working directory
        GeneralFunctions.handle_file_loc()  
        save_cwd = cwd + "\Saves"
        save_name = username.lower()
        
GeneralFunctions.start_up()
