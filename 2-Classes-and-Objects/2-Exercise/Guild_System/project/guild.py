from typing import List
from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player) -> str:
        if player in self.players:
            return f"Player {player.name} is already in the guild."

        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str) -> str:
        try:
            curr_player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        self.players.remove(curr_player)
        curr_player.guild = "Unaffiliated"
        return f"Player {curr_player.name} has been removed from the guild."

    def guild_info(self):
        players = "\n".join([p.player_info() for p in self.players])
        return f"Guild: {self.name}\n" \
               f"{players}"
