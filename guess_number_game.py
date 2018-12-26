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
    
    def increment_score(self,points=1):
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
        return self.name

    def set_guess(self, number):
        "Set the guess of the player"
        self.guess = number
        return self.guess

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
        game_continue = True
        while game_continue:
            self.start_round()       

    def print_rules(self):
        "Print the rules of the game"
        pass

    def get_players_names(self):
        "Get the player names from the user"
        for i in range(1,self.number_of_players+1):            
            self.player_name = raw_input("Hi Player enter your name")
            self.player_object = Player(self.player_name)            
            self.player_object.get_name()
            self.players.append(self.player_name)
            print self.players
        #return self.players       

    def start_round(self):
        "Start a new round"
        self.magic_number = self.generate_random_numbers()
        self.collect_guesses()
        #self.determine_winners()
        self.update_player_scores()
        self.continue_game()
        
    def generate_random_numbers(self):
        "Generate a random number"
        self.magic_number = random.randint(1,10) 
        print 'magic number is',self.magic_number       
        return self.magic_number

    def determine_winners(self,player):
        "Determine the winner(s)"        
        #for player in self.players:
        difference = abs(self.player_object.get_guess() - self.magic_number)
        if difference == self.winning_difference:
            self.winners.append(player)
        if difference < self.winning_difference:            
            self.winners = [player]
        self.winning_difference = difference
               
    def collect_guesses(self):
        "Collect the guesses"
        for player in self.players:
            self.player_guess = int(raw_input("Hi, %s Enter your guess"%player))
            self.player_object.set_guess(self.player_guess)
            self.determine_winners(player)   
        
    def update_player_scores(self):
        "Update the winners scores"
        for player in self.winners:
            self.player_object.set_name(player)
            self.player_object.increment_score(self.winning_points)

    def continue_game(self):
        "Ask players if they should continue the game"
        print("Press 'Y' if you want to continue your game")
        player_decision = raw_input()
        if player_decision == 'Y':
            self.start_round()
        else:
            self.print_result()       

    def print_result(self):
        "Print the result of the game"       
        for player in self.winners:
            print 'player',player
            print self.player_object.set_name(player)
            print self.player_object.get_score()
            if self.player_object.get_score() == self.winning_score:
                self.winners.append(player)
            if self.player_object.get_score() > self.winning_score:
                self.winners = [player]
                print self.winners
        #self.winning_score = self.player_object.get_score()
        print self.winning_score
        
        print "The winner(s) list: "
        for player in self.winners:
            print self.player_object.get_name()
            print "The winning score was:"
            self.player_object.get_score()

        """print "The scoreboard looked like this:"
        for player in self.players:
            print self.player_object.get_name(), self.player_object.get_score()"""
        
# Program starts here
if __name__ == "__main__":
    number_of_players = int(raw_input("Enter the number of players"))
    #player = Player()
    game = Game(number_of_players)
    game.print_rules()
    game.start_game()


