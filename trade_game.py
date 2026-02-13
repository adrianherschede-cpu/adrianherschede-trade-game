# Cowboys ↔ Eagles Trade Game

import random

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players

    def trade(self, other_team, player_out, player_in):
        if player_out in self.players and player_in in other_team.players:
            self.players.remove(player_out)
            other_team.players.remove(player_in)
            self.players.append(player_in)
            other_team.players.append(player_out)
            print(f"Trade Completed: {self.name} traded {player_out} for {other_team.name} {player_in}")
        else:
            print("Trade cannot be completed. Make sure the players are on the respective teams.")

def main():
    cowboys_players = ["Dak Prescott", "Ezekiel Elliott", "CeeDee Lamb"]
    eagles_players = ["Jalen Hurts", "Miles Sanders", "DeVonta Smith"]

    cowboys = Team("Dallas Cowboys", cowboys_players)
    eagles = Team("Philadelphia Eagles", eagles_players)

    print("Welcome to the Cowboys ↔ Eagles Trade Game!")

    # Example Trade
    print(f"Current Cowboys Players: {cowboys.players}")
    print(f"Current Eagles Players: {eagles.players}")

    trade_player_out = random.choice(cowboys.players)
    trade_player_in = random.choice(eagles.players)
    cowboys.trade(eagles, trade_player_out, trade_player_in)

    print(f"Final Cowboys Players: {cowboys.players}")
    print(f"Final Eagles Players: {eagles.players}")

if __name__ == "__main__":
    main()