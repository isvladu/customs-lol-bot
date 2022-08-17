import discord
from discord.ui import View
from bot.database.player_connection import PlayerConnection

from bot.utils.player import Player


class RolesSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.roles = None

    @discord.ui.select(
        placeholder="Select roles",
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
        
        select.placeholder = ", ".join(self.roles)
        self.children[1].style = discord.ButtonStyle.primary
        self.children[1].disabled = False
        self.children[1].emoji = None
        
        await interaction.response.edit_message(view=self)
        
    @discord.ui.button(label="QUEUE", style=discord.ButtonStyle.primary, disabled=True)
    async def queue_button_callback(self, button, interaction):
        button.disabled = True
        button.emoji = "<a:loading:1009553694855004291>"
        button.style = discord.ButtonStyle.success
        self.children[2].disabled = False
        
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="X", style=discord.ButtonStyle.danger, disabled=True)
    async def cancel_queue_button_callback(self, button, interaction):
        button.disabled = True
        self.children[1].style = discord.ButtonStyle.primary
        self.children[1].disabled = False
        self.children[1].emoji = None
        
        await interaction.response.edit_message(view=self)