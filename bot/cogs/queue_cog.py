import logging

import discord
from bot.configuration.config import cfg
from bot.customs_bot import CustomsBot
from bot.views.queue_init_button_view import QueueInitButtonView
from discord.ext import commands
from discord.commands import slash_command


class QueueCog(commands.Cog):
    """
    Cog managing the game queue.
    """

    def __init__(self, bot: CustomsBot):
        self.bot = bot
        self.logger = logging.getLogger(__name__)

    @commands.Cog.listener()
    async def on_ready(self):
        self.logger.info(f"Queue cog is ready!")
        
    @slash_command(guild_ids=[975367601771388968])
    async def queue(self, ctx: commands.Context):
        embed = discord.Embed(title=f"Freenatic Queue",
                              description=f"Click **Open Queue** to begin.", colour=discord.Colour.dark_grey())
        
        await ctx.respond(embed=embed, view=QueueInitButtonView())
        
    # TODO: Further queue implementation needs to be done.