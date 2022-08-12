class Player(object):
    # Class Attributes, tracking all players
    players = {}
    id_player_names = {}  # Just something to help you track id to players
    last_id = 0

    def __init__(self, name=None, height=0, weight=0, bmi=0):

        # Player attributes, tracking a player's stats
        self.name = name
        self.height = height
        self.weight = weight
        self.bmi = bmi

        self.player_id = Player.last_id + 1

        # Register the player
        Player.register_player(self.player_id, name, height, weight, bmi)

    @classmethod
    def register_player(cls, player_id, name, height, weight, bmi):

        cls.players.update({player_id:
                                {"name": name, "height": height, "weight": weight, "bmi": bmi}

                            })
        cls.id_player_names.update({player_id: name})

        cls.last_id = max(cls.id_player_names, key=int)

    @classmethod
    def list_all_players(cls):
        for player_id, name in cls.id_player_names.items():
            print("Player ID: ", player_id, "name: ", name)
            return cls.id_player_names

    @classmethod
    def list_all_players_stats(cls):
        for player_id, stats in cls.players.items():
            print("Player ID: ", player_id, stats['name'], "\n", "stats: ", stats, "\n")
        return cls.players

    @classmethod
    def update_player(cls, player_id, **kwargs):

        cls.players[player_id].update(kwargs)

        if "name" in kwargs:
            cls.id_player_names[player_id] = kwargs['name']

        # print("player_id: ", player_id, "name: ", cls.id_player_names[player_id], "has been updated")

    @classmethod
    def get_player_stats(cls, player_id):
        return cls.players[player_id]

    def stats(self):
        return Player.get_player_stats(self.player_id)

    def get_height(self):
        height = float(input("Please enter player's height in metres: "))
        self.height = height
        Player.update_player(self.player_id, height=height)

        return height

    def get_weight(self):
        weight = float(input("Please enter player's weight in kg: "))
        self.weight = weight

        Player.update_player(self.player_id, weight=weight)

        return weight

    @staticmethod
    def calculate_bmi(height, weight):

        bmi = round((weight / (height*height)), 1)

        return bmi

    def get_bmi(self):
        if self.height is 0:
            self.get_height()
        if self.weight is 0:
            self.get_weight()

        bmi = self.calculate_bmi(self.height, self.weight)
        Player.update_player(self.player_id, bmi=bmi)
        self.bmi = bmi

        return self.bmi


# Example use case
if __name__ == '__main__':
    players_added = 0
    while True:

        if players_added == 5:
            print("Total roster of players added \n")
            print(Player.list_all_players())
            players_added = 0

        name = input("What is the player's name?: ")
        a_player = Player(name)
        a_player.get_bmi()

        print("Displaying {}'s stats".format(name))
        print(a_player.stats(), "\n")

        print("Listing all player's stats")
        Player.list_all_players_stats()

        players_added += 1
