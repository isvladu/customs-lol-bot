import logging

import discord
from discord.ext import commands

from bot.configuration.config import cfg
from bot.views.register_button_view import RegisterButtonView

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

        self.add_cog(RegistrationCog(self))

    async def on_ready(self):
        self.logger.info(f"Logged in as {self.user}")

        embed = discord.Embed(title=f"Test registration embed",
                              description=f"Test description", colour=discord.Colour.blue())
        channel_id = cfg["app"]["reg_chan_id"]
        channel = self.get_channel(int(channel_id))
        self.logger.info(f"{channel} - {int(channel_id)}")

        await channel.send(embed=embed, view=RegisterButtonView())

    def run(self, *args, **kwargs):
        super().run(cfg["app"]["token"], *args, **kwargs)
