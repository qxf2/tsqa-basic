"""
Players should guess the number if it matches approx with magical number
then the player score will get incremented.If the players wanted to continue
the game they can continue or they can stop the program.Once the game is stopped
final winner and score will be displayed
"""

import random

class Player: 
    "The player class"
    def __init__(self,name):
        "Initializer"
        self.name = name 
        self.score = 0
        self.guess = None 
    
    def increment_score(self,points):
        "Add points to the player's score"
        self.score += points
       
    def get_score(self):
        "Return the score"
        return self.score    

    def get_name(self):
        "Return the name of the player"
        return self.name
    
    def set_name(self,name):
        "Set the name of the player"
        self.name = name       

    def set_guess(self, number):
        "Set the guess of the player"
        self.guess = number
        
    def get_guess(self):
        "Get the player's current guess"
        return self.guess


class Game:
    "The game class"
    def __init__(self,number_of_players):
        "Initializer"
        self.number_of_players = number_of_players
        self.players = []
        self.winners = []
        self.magic_number = -1
        self.winning_points = 1 #number of points you score when you win a round
        self.winning_difference = 10000
        self.winning_score = -1

    def start_game(self):
        "Start the game"
        self.get_players_names()                     
        self.start_play()        
        self.continue_game()
        self.determine_final_game_winner()
        self.print_result()

    def print_rules(self):
        "Print the rules of the game"
        print('1.Each player can enter one number at a time')
        print('2.Player 2 cannot repeat the same number of player 1')
        print('3.Enter the number between 1 to 10 only')

    def get_players_names(self):
        "Get the player names from the user"
        for i in range(0,self.number_of_players):            
            player_name = raw_input("Hi Player enter your name")
            player_object = Player(player_name)           
            self.players.append(player_object)
            
    def start_play(self):
        "Start a new round"    
        self.generate_random_numbers()
        self.collect_guesses()
        self.determine_winners()
        self.update_player_scores()               
        
    def generate_random_numbers(self):
        "Generate a random number"
        self.magic_number = random.randint(1,10)               
        return self.magic_number

    def determine_winners(self):
        "Determine the winner(s)"
        self.winners = []
        winning_difference = 10000
        for player in self.players:
            difference = abs(player.get_guess() - self.magic_number)           
            if difference == winning_difference:
                self.winners.append(player)
            if difference < winning_difference:
                self.winners = [player]
            winning_difference = difference        
        
    def collect_guesses(self):
        "Collect the guesses"
        for player in self.players:
            player_guess = int(raw_input("Hi Player,Enter your guess"))
            player.set_guess(player_guess)
           
    def update_player_scores(self):
        "Update the winners scores"
        for player in self.winners:           
            player.increment_score(self.winning_points)              
            print('The winner of the round score is',player.get_score(),player.get_name())        

    def continue_game(self):
        "Ask players if they should continue the game"
        print("Press 1 to continue your game or press 2 to stop the game")
        game_choice = input()
        if game_choice == 1:
            self.start_play()
            self.continue_game()
        else:
            print("You have decided to stop the game,Now you can view your score board")        
        
    def determine_final_game_winner(self):
        "Determine the final winner of the game"        
        self.winners = []
        winning_score = -1
        for player in self.players:
            if player.get_score() == winning_score:
                self.winners.append(player)
            if player.get_score() > winning_score:
                self.winners = [player]        
        
    def print_result(self):
        "Print the result of the game"        
        print("The winner(s) list: ")
        for player in self.winners:
            print player.get_name()
        print("The winning score was:")
        player.get_score()

        print("The scoreboard looked like this:")
        for player in self.players:
            print player.get_name(), player.get_score()
        
# Program starts here
if __name__ == "__main__":
    number_of_players = int(raw_input("Enter the number of players"))    
    game = Game(number_of_players)
    game.print_rules()
    game.start_game()


