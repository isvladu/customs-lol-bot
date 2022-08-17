import discord
from bot.database.player_connection import PlayerConnection
from bot.modals.summoner_modal import SummonerModal
from bot.utils.player import Player
from bot.views.role_select_view import RolesSelectView
from discord.ui import View


class RegisterButtonView(View):
    def __init__(self, connection: PlayerConnection):
        super().__init__(timeout=None)
        self.connection = connection
        self.roles = None
        self.summoner_name = None
        self.elo = None
        # summonerButton = discord.ui.Button(label="Test link", style=discord.ButtonStyle.link, url="https://discord.com/channels/975367601771388968/1009218791911215205")
        # self.add_item(summonerButton)

    @discord.ui.button(label="Register", style=discord.ButtonStyle.primary)
    async def summoner_button_callback(self, button, interaction):
        modal = SummonerModal()
        view = RolesSelectView()

        await interaction.response.send_modal(modal)
        await interaction.followup.send("Please fill in your roles below (min 1, max 5).", view=view, ephemeral=True)
        
        await modal.wait()
        await view.wait()
        
        self.roles = view.roles
        self.summoner_name = modal.summoner_name
        self.elo = modal.elo

        print(f"{self.roles} - {self.summoner_name} - {self.elo}")

    @discord.ui.button(label="Verify", style=discord.ButtonStyle.primary)
    async def verify_button_callback(self, button, interaction):
        current_player = Player(_id=interaction.user.id, name=interaction.user.name, roles=self.roles, summoner_name=self.summoner_name, elo=self.elo)
        
        if current_player.isValid():
            thumbnail_file = discord.File()
            role_files = []
            embed = discord.Embed(title=f"Player Verification", description=f"<@{interaction.user.id}>")
            embed.add_field(name="League IGN", value=current_player.summoner_name, inline=False)
            embed.add_field(name="Roles", value=current_player.roles, inline=False)
            embed.add_field(name="Elo", value=str(current_player.elo), inline=False)
            await interaction.response.send_message(embed=embed, ephemeral=True)
        else:
            await interaction.response.send_message("You can't verify", ephemeral=True)

    # TODO: finish the verification embed (files, thumbnail, images, etc)
    # TODO: add mongoDB sync again
