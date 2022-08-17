import discord
from bot.configuration.config import cfg
from bot.database.player_connection import PlayerConnection
from bot.modals.summoner_modal import SummonerModal
from bot.utils.player import Player
from bot.utils.summoner import Summoner
from bot.views.role_select_view import RolesSelectView
from bot.views.validate_button_view import ValidateButtonView
from discord.ui import View


class RegisterButtonView(View):
    def __init__(self, connection: PlayerConnection):
        super().__init__(timeout=None)
        
        self.connection = connection
        self.roles = None
        self.summoner_name = None
        self.elo = None
        self.rank = None

    @discord.ui.button(label="REGISTER", style=discord.ButtonStyle.primary)
    async def summoner_button_callback(self, button, interaction):
        if interaction.user.get_role(int(cfg["app"]["member_role_id"])) is not None:
            for child in self.children:
                child.disabled = True
                child.style = discord.ButtonStyle.danger
            embed = discord.Embed(title=f"Summoner Registration",
                              description=f"You are already registered!", colour=discord.Colour.dark_grey())
            await interaction.response.edit_message(embed=embed, view=self)
            return
            
        modal = SummonerModal()
        await interaction.response.send_modal(modal)
        await modal.wait()

        self.summoner_name = modal.summoner_name
        self.elo = modal.elo
        self.rank = modal.rank
        
    @discord.ui.button(label="VERIFY", style=discord.ButtonStyle.primary)
    async def verify_button_callback(self, button, interaction):
        current_player = Player(_id=interaction.user.id, name=interaction.user.name,
                                summoner_name=self.summoner_name, rank=self.rank, elo=self.elo, wins=0, losses=0)

        if current_player.isValid() and interaction.user.get_role(int(cfg["app"]["member_role_id"])) is None:
            file = discord.File(Summoner.getSummonerTierURL(
                rank=current_player.rank), filename=f"{current_player.rank}.png")

            embed = discord.Embed(
                title=f"Player Verification", description=f"<@{interaction.user.id}>")
            embed.set_thumbnail(url=f"attachment://{current_player.rank}.png")
            embed.add_field(name="League IGN",
                            value=current_player.summoner_name, inline=False)
            embed.add_field(name="Server", value="EUNE", inline=False)
            embed.add_field(name="Elo", value=str(
                current_player.elo), inline=False)

            await interaction.response.send_message(file=file, embed=embed, view=ValidateButtonView(player=current_player, connection=self.connection), ephemeral=True)
        elif interaction.user.get_role(int(cfg["app"]["member_role_id"])) is not None:
            for child in self.children:
                child.disabled = True
                child.style = discord.ButtonStyle.danger
            embed = discord.Embed(title=f"Summoner Registration",
                              description=f"You are already registered!", colour=discord.Colour.dark_grey())
            await interaction.response.edit_message(embed=embed, view=self)
        else:
            embed = discord.Embed(title=f"Summoner Registration",
                              description=f"Please click the registration button first!", colour=discord.Colour.dark_grey())
            await interaction.response.edit_message(embed=embed, view=self)
