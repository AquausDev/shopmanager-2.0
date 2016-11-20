class VariableHandling():
    """Runs the init and mangement of variables"""
    @staticmethod
    def init_varibles():
        global username
        username = input("What is your name? ")

class GeneralFunctions():
    """Runs the functions that control the game"""

class GameManagement():
    """Runs the management of the game"""
    @staticmethod
    def run_game():
        VariableHandling.init_varibles()

class DataHandling():
    """Runs functions such as saving, loading and qutting"""
    
GameManagement.run_game()
