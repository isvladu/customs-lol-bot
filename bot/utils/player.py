import logging
from typing import List

from bot.utils.role import Role

logger = logging.getLogger(__name__)


class Player:
    """
    Class representation of a player.
    """

    _id: int
    _name: str
    roles: List[Role]
    elo: float
    summoner_name: str

    def __init__(self, _id: int, name: str, roles: List[str] = None, elo: float = None, summoner_name: str = None):
        self._id = _id
        self._name = name
        self.roles = []
        self.elo = elo
        self.summoner_name = summoner_name

        if roles is not None:
            self.addRoles(roles)

    def __eq__(self, other):
        if isinstance(other, Player):
            return self.id == other.id
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def addRole(self, role: str):
        """Adds a role to the role list of the player.

        Args:
            role (str): Singular role to be added
        """        
        if role in self.roles:
            logger.error(f"Role {role.name} is already registered")
            return
        logger.info(f"Role {role.name} has been registered")
        self.roles.append(role)

    def addRoles(self, role_list: list[str]):
        for role in role_list:
            self.addRole(role)

    def removeRole(self, role: str):
        if role not in self.roles:
            logger.error(f"Role {role.name} is not registered")
            return
        logger.info(f"Role {role} has been removed")
        self.roles.remove(role)

    def removeRoles(self, role_list: list[str]):
        for role in role_list:
            self.removeRole(role)

    def getRoles(self):
        return [role.name for role in self.roles]

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    # Encoding Player() object for MongoDB queries
    def encode_player(self):
        return {"_id": self._id, "name": self._name, "roles": self.getRoles(), "elo": self.elo,
                "summoner_name": self.summoner_name}
