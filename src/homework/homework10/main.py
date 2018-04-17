from src.homework.homework10.player import Player
#write import statement for GameLog class
from src.homework.homework10.game_log import GameLog

class Main:
#Create a game log instance
    game_log = GameLog()

#SEnd the game_log instance to Player class as an argument
    player = Player
    player(game_log).roll_doubles()
    


#call the game log display method below
    game_log.display_log



Main()
