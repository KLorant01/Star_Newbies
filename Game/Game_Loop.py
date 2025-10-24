from Resources.Data.VARIABLES import SAVING_FILE, AUTOSAVE
from Resources.Data.Enums import MainSt, GameSt
from Game.Game_States.Main_Screen import MainScreen
from Resources.Data.VARIABLES import GAME_IN_PROGRESS_SWITCH
from Modules.Characters.Crew import Crew
import logging as lg
import pickle


STARTING_CREW_SIZE: int = 4


class GameLoop:
    def __init__(self, game_surface, screen, clock, screenwidth, screenheight):
        lg.debug("init")

        self.game_surface = game_surface
        self.screenWidth = screenwidth
        self.screenHeight = screenheight
        self.screen = screen
        self.clock = clock

        #GAME OBJECTS:
        self.game_data = {
            "ship" : None,
            "inventory": None,
            "map": None,
            "crew": Crew(STARTING_CREW_SIZE)
        }

        lg.info(self.game_data["crew"])


    def loop(self):
        game_state = GameSt.MAIN_SCREEN

        # Load game if possible
        if AUTOSAVE:
            with open(GAME_IN_PROGRESS_SWITCH, "r") as File:
                if bool(File.read()):
                    self.load_game()

        while 1:
            match game_state:
                case GameSt.MAIN_SCREEN:
                    lg.debug("Go to GameSt.MAIN_SCREEN")
                    game_state = MainScreen(self.game_surface, self.screen, self.clock, self.screenWidth, self.screenHeight).main()

                case GameSt.SHIP:
                   lg.debug("Go to GameSt.SHIP")
                   raise NotImplementedError("Feature GameSt.SHIP not implemented yet")

                case GameSt.INVENTORY:
                   lg.debug("Go to GameSt.INVENTORY")
                   raise NotImplementedError("Feature GameSt.INVE not implemented yet")

                case GameSt.CHARACTERS:
                   lg.debug("Go to GameSt.CHARACTERS")
                   raise NotImplementedError("Feature GameSt.CHAR not implemented yet")

                case GameSt.SETTINGS:
                   lg.debug("Go to GameSt.SETTINGS")
                   self.save_game()
                   raise NotImplementedError("Feature GameSt.SETT not implemented yet")

                case GameSt.MISSIONS:
                   lg.debug("Go to GameSt.MISSIONS")
                   raise NotImplementedError("Feature GameSt.PROC not implemented yet")

                case GameSt.FIGHT:
                   lg.debug("Go to GameSt.FIGHT")
                   raise NotImplementedError("Feature GameSt.FIGH not implemented yet")

                case MainSt.MAIN_MENU:
                    if AUTOSAVE:
                        self.save_game()
                    return MainSt.MAIN_MENU


    def save_game(self):
        lg.info("Save")
        with open(SAVING_FILE, "wb") as saveFile:
            pickle.dump(self.game_data, file=saveFile)

        with open(GAME_IN_PROGRESS_SWITCH, "w") as File:
            File.write("True")


    def load_game(self):
        lg.info("Load game")
        with open(SAVING_FILE, "rb") as saveFile:
            self.game_data = pickle.load(saveFile)
