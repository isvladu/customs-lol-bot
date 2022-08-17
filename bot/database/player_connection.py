from typing import Optional

from bot.database.connection import Connection
from bot.utils.player import Player


class PlayerConnection(Connection):
    """
    Represents the connection handling of operations with the Players table.
    """

    def __init__(self):
        super().__init__()
        self.table = super().getCollection("players")

    @staticmethod
    def decodePlayer(document) -> Optional[Player]:
        """Decodes the BSON document that a MongoDB query returns into a Player object.

        Args:
            document (Any | None): The BSON document returned by a MongoDB query

        Returns:
            Optional[Player]: Player object to be returned if valid, else None
        """
        if document is None:
            return None
        else:
            return Player(document["_id"], document["name"], document["summoner_name"], document["rank"], 
                          document["elo"], document["wins"], document["losses"])

    def getPlayer(self, unique_id: int) -> Optional[Player]:
        """Returns the Player associated with the given ID.

        Args:
            unique_id (int): Unique ID of the queried player

        Returns:
            Optional[Player]: Player object if the player was found, else None
        """
        return self.decodePlayer(self.table.find_one({"_id": unique_id}))

    def insertPlayer(self, player: Player) -> None:
        """Inserts a player into the database.

        Args:
            player (Player): Player to be inserted into the database.
        """
        self.table.insert_one(player.encode_player())

    def updatePlayerStats(self, _id: str, elo: int, wins: int, losses: int) -> None:
        """Updates the ELO, wins and losses of a player in the database.

        Args:
            _id (str): ID of the player to be updated
            elo (int): ELO to be updated in the database
            wins (int): Wins to be updated in the database
            losses (int): Losses to be updated in the database
        """
        query = {"_id": _id}
        values = {"$set": {"elo": elo, "wins": wins,
                           "losses": losses}}

        self.table.update_one(query, values)
