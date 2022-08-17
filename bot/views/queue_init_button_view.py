import discord

from discord.ui import View

from bot.views.role_select_view import RolesSelectView

class QueueInitButtonView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
        leaderboardButton = discord.ui.Button(label="Leadboard", style=discord.ButtonStyle.link, url="https://google.com")
        self.add_item(leaderboardButton)
        
    @discord.ui.button(label="Open Queue", style=discord.ButtonStyle.primary)
    async def open_queue_button_callback(self, button, interaction):
        embed = discord.Embed(
                title=f"Solo Queue", description=f"<@{interaction.user.id}>")
        view = RolesSelectView()
        
        await interaction.response.send_message(embed=embed, view=view, ephemeral=True)