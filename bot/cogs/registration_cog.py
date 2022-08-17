import logging

import discord
from bot.configuration.config import cfg
from bot.customs_bot import CustomsBot
from bot.database.player_connection import PlayerConnection
from bot.views.register_button_view import RegisterButtonView
from discord.ext import commands
from discord.ui import Modal


class RegistrationCog(commands.Cog):
    """
    Cog managing player registration.
    """

    def __init__(self, bot: CustomsBot):
        self.bot = bot
        self.connection = PlayerConnection()
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f"Registration cog is ready!")

        embed = discord.Embed(title=f"Test registration embed",
                              description=f"Test description", colour=discord.Colour.blue())
        channel_id = int(cfg["app"]["reg_chan_id"])
        channel = self.bot.get_channel(channel_id)

        await channel.send(embed=embed, view=RegisterButtonView(self.connection))
