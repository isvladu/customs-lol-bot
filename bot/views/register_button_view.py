import discord
from discord.ui import View

from bot.modals.summoner_modal import SummonerModal
from bot.views.role_select_view import RolesSelectView


class RegisterButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
        summonerButton = discord.ui.Button(label="Test link", style=discord.ButtonStyle.link, url="https://discord.com/channels/975367601771388968/1009218791911215205")
        self.add_item(summonerButton)

    @discord.ui.button(label="Add summoner", style=discord.ButtonStyle.primary)
    async def summoner_button_callback(self, button, interaction):
        modal = SummonerModal()
        await interaction.response.send_modal(modal)

    @discord.ui.button(label="Add roles", style=discord.ButtonStyle.primary)
    async def roles_button_callback(self, button, interaction):
        await interaction.response.send_message("Test", view=RolesSelectView(), ephemeral=True)