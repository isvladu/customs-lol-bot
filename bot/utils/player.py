import logging
from typing import List

logger = logging.getLogger(__name__)


class Player:
    """
    Class representation of a player.
    """

    _id: int
    _name: str
    summoner_name: str
    rank: str
    elo: int
    wins: int
    losses: int

    def __init__(self, _id: int, name: str, summoner_name: str = None, rank: str = None, elo: int = None, wins: int = 0, losses: int = 0):
        self._id = _id
        self._name = name
        self.summoner_name = summoner_name
        self.rank = rank
        self.elo = elo
        self.wins = wins
        self.losses = losses

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def isValid(self):
        return self.summoner_name is not None

    # Encoding Player object for MongoDB queries
    def encode_player(self):
        return {"_id": self._id, "name": self._name, "summoner_name": self.summoner_name,
                "rank": self.rank, "elo": self.elo, "wins": self.wins, "losses": self.losses
                }
