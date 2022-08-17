import logging

import discord
from discord.ext import commands

from bot.configuration.config import cfg

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

        from bot.cogs.registration_cog import RegistrationCog
        from bot.cogs.queue_cog import QueueCog

        self.add_cog(RegistrationCog(self))
        self.add_cog(QueueCog(self))

    async def on_ready(self):
        self.logger.info(f"Logged in as {self.user}")

    def run(self, *args, **kwargs):
        super().run(cfg["app"]["token"], *args, **kwargs)

# TODO: create slash commands to initiliaze the registration and queue