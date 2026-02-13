# Cowboys ↔ Eagles Trade Game

from dataclasses import dataclass, field
from typing import List, Dict, Tuple
import random

@dataclass
class Player:
    name: str
    position: str
    value: int

@dataclass
class Team:
    name: str
    players: List[Player] = field(default_factory=list)
    draft_picks: int = 0

@dataclass
class TradeProposal:
    offering_team: Team
    receiving_team: Team
    offered_players: List[Player]
    requested_players: List[Player]
    draft_picks: int = 0

class TradeGame:
    def __init__(self, team_a: Team, team_b: Team):
        self.team_a = team_a
        self.team_b = team_b
        self.current_team = team_a

    def display_teams(self):
        print(f"{self.team_a.name} Players:")
        for player in self.team_a.players:
            print(f"- {player.name} ({player.position}): {player.value}")

        print(f"\n{self.team_b.name} Players:")
        for player in self.team_b.players:
            print(f"- {player.name} ({player.position}): {player.value}")

    def propose_trade(self, proposal: TradeProposal):
        print(f"Trade Proposal from {proposal.offering_team.name} to {proposal.receiving_team.name}:")
        print(f"Offering Players:")
        for player in proposal.offered_players:
            print(f"- {player.name} ({player.position})")
        print(f"Requesting Players:")
        for player in proposal.requested_players:
            print(f"- {player.name} ({player.position})")
        print(f"Offering {proposal.draft_picks} draft pick(s).\n")
        self.evaluate_trade(proposal)

    def evaluate_trade(self, proposal: TradeProposal):
        # Simulate CPU decision logic
        trade_value = sum(player.value for player in proposal.offered_players) - \
                      sum(player.value for player in proposal.requested_players) + proposal.draft_picks
        print(f"Trade Value Calculation: {trade_value}")
        decision = random.choice([True, False])
        if trade_value > 0:
            decision = True
        if decision:
            self.accept_trade(proposal)
        else:
            print(f"Trade declined by {proposal.receiving_team.name}.")
            self.counteroffer(proposal)

    def accept_trade(self, proposal: TradeProposal):
        for player in proposal.offered_players:
            proposal.receiving_team.players.append(player)
            proposal.offering_team.players.remove(player)
        for player in proposal.requested_players:
            proposal.offering_team.players.append(player)
            proposal.receiving_team.players.remove(player)
        proposal.offering_team.draft_picks -= proposal.draft_picks
        proposal.receiving_team.draft_picks += proposal.draft_picks
        print(f"Trade accepted! {proposal.offering_team.name} traded {len(proposal.offered_players)} players and {proposal.draft_picks} draft pick(s) to {proposal.receiving_team.name}.")

    def counteroffer(self, proposal: TradeProposal):
        print(f"{proposal.receiving_team.name} makes a counteroffer.")
        if proposal.offering_team.name == self.team_a.name:
            # Example logic for counteroffer
            counter_player = self.team_b.players[0]  # Just a placeholder
            print(f"Counteroffer: Trade {counter_player.name} for {proposal.offered_players[0].name}.")

# Example Usage
if __name__ == '__main__':
    cowboys = Team(name='Cowboys')
    eagles = Team(name='Eagles')

    # Sample players
    cowboys.players = [Player(name='Dak Prescott', position='QB', value=90), 
                       Player(name='Ezekiel Elliott', position='RB', value=85)]
    eagles.players = [Player(name='Jalen Hurts', position='QB', value=88), 
                      Player(name='DeVonta Smith', position='WR', value=80)]

    # Initialize game
    game = TradeGame(cowboys, eagles)
    game.display_teams()

    # Propose a trade
    trade_proposal = TradeProposal(offering_team=cowboys, \n                                   receiving_team=eagles, \
                                   offered_players=[cowboys.players[1]], \
                                   requested_players=[eagles.players[0]], \
                                   draft_picks=1)
    game.propose_trade(trade_proposal)