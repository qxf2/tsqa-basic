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
