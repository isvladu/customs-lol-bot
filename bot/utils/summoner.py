import random
from typing import Tuple, Dict

import requests

from bot.configuration.config import cfg


class Summoner:
    """
    Class that validates when a summoner is added.
    """

    icon_id: int
    summoner_name: str
    headers: Dict[str, str]
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
        self.rank = self.getSummonerTier()

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
    
    @staticmethod
    def getSummonerTierURL(rank: str) -> str:
        """Returns the url for the tier icon.

        Returns:
            str: Rank of the player
        """        
        return "images/tiers/" + str(rank) + ".png"
    
    def getSummonerTier(self) -> str:
        """Returns the tier of the summoner.

        Returns:
            str: The tier to be returned
        """        
        acc_id = requests.get(url=self.account_endpoint+self.summoner_name, headers=self.headers).json()["id"]
        rank_data = requests.get(url=self.ranked_endpoint+acc_id, headers=self.headers).json()
        
        for queue in rank_data:
            if queue["queueType"] == "RANKED_SOLO_5x5":
                return queue["tier"]
        
        return "BRONZE"

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
            return 1500, 0
        else:
            return r.json()["ranked"]["avg"], r.json()["ranked"]["err"]
        