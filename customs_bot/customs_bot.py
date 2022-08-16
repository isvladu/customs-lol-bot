import logging

import discord
from discord.ext import commands

from configuration.config import cfg

intents = discord.Intents.default()
intents.members = True


class CustomsBot(commands.Bot):
    """
    Bot handling role-based matchmaking for Custom League of Legends games
    """

    def __init__(self, **options):
        super().__init__(cfg["app"]["prefix"],
                         intents=intents, case_insensitive=True, **options)

        self.logger = logging.getLogger(__name__)

    async def on_ready(self):
        self.logger.info(f"Logged in as {self.user}")

    def run(self, *args, **kwargs):
        super().run(cfg["app"]["token"], *args, **kwargs)
