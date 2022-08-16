import discord
from discord.ui import View


class RolesSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        
    @discord.ui.select(
        placeholder = "Choose your roles",
        min_values = 1,
        max_values = 5,
        options = [
            discord.SelectOption(label="Top"),
            discord.SelectOption(label="Jungle"),
            discord.SelectOption(label="Mid"),
            discord.SelectOption(label="Bot"),
            discord.SelectOption(label="Support")
        ]
    )
    async def select_callback(self, select, interaction):
        await interaction.response.send_message(f"You selected {select.values}", ephemeral=True)