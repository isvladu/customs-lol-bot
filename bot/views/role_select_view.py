import discord
from discord.ui import View
from bot.database.player_connection import PlayerConnection

from bot.utils.player import Player


class RolesSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.roles = None

    @discord.ui.select(
        placeholder="Choose your roles",
        min_values=1,
        max_values=5,
        options=[
            discord.SelectOption(label="TOP"),
            discord.SelectOption(label="JUNGLE"),
            discord.SelectOption(label="MID"),
            discord.SelectOption(label="BOT"),
            discord.SelectOption(label="SUPPORT")
        ]
    )
    async def select_callback(self, select, interaction):
        self.roles = select.values
        
        await interaction.response.defer()

        self.stop()