import discord
from bot.configuration.config import cfg
from bot.database.player_connection import PlayerConnection
from bot.utils.player import Player
from discord.ui import View


class ValidateButtonView(View):
    def __init__(self, player: Player, connection: PlayerConnection):
        super().__init__(timeout=None)
        self.player = player
        self.connection = connection

    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.primary)
    async def confirm_button_callback(self, button, interaction: discord.Interaction):
        self.connection.insertPlayer(self.player)
        role = interaction.guild.get_role(int(cfg["app"]["member_role_id"]))

        await interaction.user.add_roles(role)
        await interaction.response.send_message("You have succesfully registered!", ephemeral=True)

    @discord.ui.button(label="Cancel", style=discord.ButtonStyle.danger)
    async def cancel_button_callback(self, button, interaction):
        await interaction.response.send_message("You have canceled the registration!", ephemeral=True)
