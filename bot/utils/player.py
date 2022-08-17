import logging
from typing import List

logger = logging.getLogger(__name__)


class Player:
    """
    Class representation of a player.
    """

    _id: int
    _name: str
    roles: List[str]
    elo: float
    summoner_name: str

    def __init__(self, _id: int, name: str, roles: List[str] = None, elo: float = None, summoner_name: str = None):
        self._id = _id
        self._name = name
        self.roles = roles
        self.elo = elo
        self.summoner_name = summoner_name

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
        if self.roles is not None and self.summoner_name is not None and self.elo is not None:
            return True
        return False

    # Encoding Player() object for MongoDB queries
    def encode_player(self):
        return {"_id": self._id, "name": self._name, "roles": self.roles, "elo": self.elo,
                "summoner_name": self.summoner_name}
