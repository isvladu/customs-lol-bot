import random
from typing import Tuple

import requests

from bot.configuration.config import cfg


class Summoner:
    """
    Class that validates when a summoner is added.
    """

    icon_id: int
    summoner_name: str
    timer: int

    account_endpoint: str = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/"
    ranked_endpoint: str = "https://eun1.api.riotgames.com/lol/league/v4/entries/by-summoner/"
    mmr_endpoint: str = "https://eune.whatismymmr.com/api/v1/summoner?name="
    icon_url: str = "images/profile_icons/"

    def __init__(self, summoner_name: str):
        self.icon_id = random.randint(1, 10)
        self.summoner_name = summoner_name
        self.headers = {"X-Riot-Token": cfg["riot"]["token"]}
        self.timer = 30

    def getSummonerIconURL(self) -> str:
        """Returns the url for the summoner icon.

        Returns:
            str: URL of the summoner icon
        """
        return self.icon_url + str(self.icon_id) + ".png"

    def getSummonerIcon(self) -> int:
        """Returns the ID of the current icon the summoner holds.

        Returns:
            int: ID of the current icon
        """
        url = self.account_endpoint + self.summoner_name

        r = requests.get(url=url, headers=self.headers)

        return r.json()["profileIconId"]
    
    def getSummonerRank(self) -> str:
        pass

    def validateSummoner(self) -> bool:
        """Validates if the assigned summoner icon matches the one the summoner has.

        Returns:
            bool: True if they match, else False
        """
        return self.getSummonerIcon() == self.icon_id

    def getSummonerMMR(self) -> Tuple[int, int]:
        """Returns the calculated MMR for the current summoner.

        Returns:
            Tuple[int, int]: (Average MMR, MMR error rate) if valid, else (1000, 0)
        """
        url = self.mmr_endpoint + self.summoner_name

        r = requests.get(url=url)
        
        if "error" in r.json().keys():
            return 1000, 0
        else:
            return r.json()["ranked"]["avg"], r.json()["ranked"]["err"]
        
    #TODO: refactor this class to contain methods to get ProfileIcon, RankedTier and return proper URLS and filenames.
