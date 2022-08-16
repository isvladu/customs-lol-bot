import logging
import random
import string
from typing import Dict, Tuple

from player import Player
from role import Role

logger = logging.getLogger(__name__)


class Match:
    """
    Class representing a match currently running.
    """

    game_id: int
    game_passwd: str
    blue_team: Dict[Role, Player]
    red_team: Dict[Role, Player]
    outcome: bool  # 0 if blue is the winner, else 1

    def __init__(self, game_id: int, blue_team: dict(Role, Player), red_team: dict(Role, Player)):
        self.blue_team = blue_team
        self.red_team = red_team
        self.game_passwd = random.choices(
            string.ascii_letters + string.digits, k=8)

    def getGameId(self) -> str:
        """Returns the game ID to be used in the creation of the game.

        Returns:
            str: ID of the game
        """
        return f"inhouse{str(self.game_id)}"

    def getGamePassword(self) -> str:
        """Returns the game password.

        Returns:
            str: Game password to be returned (8 character alphanumeric)
        """
        return self.game_passwd

    def getTeamResults(self) -> Tuple[Dict[Role, Player], Dict[Role, Player]]:
        """Returns a tuple containing the teams ordered by the outcome of the match.

        Returns:
            Tuple[Dict[Role, Player], Dict[Role, Player]]: Tuple (winning team, losing team)
        """        
        if self.outcome == 0:
            return self.blue_team, self.red_team
        return self.red_team, self.blue_team
