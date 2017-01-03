import os

class VariableHandling():
    """Runs the init and mangement of variables"""
    @staticmethod
    def init_varibles():
        global username
        username = input("What is your name? ")

class GeneralFunctions():
    """Runs the functions that control the game"""
    @staticmethod
    def first_check():
        local_dir = cwd + "first_time.check"
        data = open(local_dir, "wr")
        print(data)
        if data == "TRUE":
            #TODO: add in tutorial or firsttime load code
            first_time = "FALSE"
        
    @staticmethod
    def handle_file_loc():
        cwd = os.getcwd()
        cwd += "\Data"
        
class GameManagement():
    """Runs the management of the game"""
    @staticmethod
    def run_game():
        VariableHandling.init_varibles()

class DataHandling():
    """Runs functions such as saving, loading and qutting"""
    def save_data():
        #rechecks the current working directory
        GeneralFunctions.handle_file_loc()  
        save_cwd = cwd + "\Saves"
  
GameManagement.run_game()
