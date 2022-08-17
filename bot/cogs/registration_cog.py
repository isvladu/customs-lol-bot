import logging

import discord
from bot.configuration.config import cfg
from bot.customs_bot import CustomsBot
from bot.database.player_connection import PlayerConnection
from bot.views.register_button_view import RegisterButtonView
from discord.ext import commands
from discord.ui import Modal
from discord.commands import slash_command


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

    @slash_command(guild_ids=[975367601771388968])
    async def register(self, ctx: commands.Context):
        embed = discord.Embed(title=f"Summoner Registration",
                              description=f"Please click the REGISTER button to start the process.", colour=discord.Colour.dark_grey())
        
        await ctx.respond(embed=embed, view=RegisterButtonView(self.connection))