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
    def decode_player(document) -> Optional[Player]:
        """Decodes the BSON document that a MongoDB query returns into a Player object.

        Args:
            document (Any | None): The BSON document returned by a MongoDB query

        Returns:
            Optional[Player]: Player object to be returned if valid, else None
        """
        if document is None:
            return None
        else:
            return Player(document["_id"], document["name"], document["roles"], document["elo"],
                          document["summoner_name"])

    def getPlayer(self, unique_id: int) -> Optional[Player]:
        """Returns the Player associated with the given ID.

        Args:
            unique_id (int): Unique ID of the queried player

        Returns:
            Optional[Player]: Player object if the player was found, else None
        """
        return self.decode_player(self.table.find_one({"_id": unique_id}))

    def insertPlayer(self, player: Player):
        """Inserts a player into the database.

        Args:
            player (Player): Player to be inserted into the database.
        """
        self.table.insert_one(player.encode_player())

    def updatePlayer(self, player: Player):
        """Updates multiple fields of a player in the database.

        Args:
            player (Player): Player to be updated in the database.
        """
        query = {"_id": player.id}
        values = {"$set": {"roles": player.getRoles(), "elo": player.elo,
                           "summoner_name": player.summoner_name}}

        self.table.update_one(query, values)

    def updatePlayerRoles(self, _id: str, roles: list[str]):
        """Updates the roles of a player in the database.

        Args:
            _id (str): ID of the player to be updated
            roles (list[str]): Roles to be updated in the database
        """
        query = {"_id": _id}
        values = {"$set": {"roles": roles}}

        self.table.update_one(query, values)

    def updatePlayerElo(self, _id: str, elo: int):
        """Updates the ELO of a player in the database.

        Args:
            _id (str): ID of the player to be updated
            elo (int): ELO to be updated in the database
        """
        query = {"_id": _id}
        values = {"$set": {"elo": elo}}

        self.table.update_one(query, values)

    def updatePlayerSummonerName(self, _id: str, summoner_name: str):
        """Updates the summoner name of a player in the database.

        Args:
            _id (str): ID of the player to be updated
            summoner_name (str): Summoner name to be updated in the database
        """
        query = {"_id": _id}
        values = {"$set": {"summoner_name": summoner_name}}

        self.table.update_one(query, values)
