import logging

import discord
from discord.ext import commands

from database.player_connection import PlayerConnection
from ..customs_bot import CustomsBot

class RegistrationCog(commands.Cog):
    """
    Manages player registration
    """
    
    def __init__(self, bot: CustomsBot):
        self.bot = bot
        self.connection = PlayerConnection()
        self.logger = logging.getLogger(__name__)