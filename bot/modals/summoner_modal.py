import asyncio
import discord
from bot.database.player_connection import PlayerConnection
from bot.utils.player import Player
from discord.ui import InputText, Modal

from bot.utils.summoner import Summoner


class SummonerModal(Modal):
    def __init__(self) -> None:
        super().__init__(title="Summoner Registration Modal")
        self.summoner_name = None
        self.elo = None
        self.rank = None

        self.add_item(InputText(label="Summoner name",
                      placeholder="Your summoner name"))

    async def callback(self, interaction: discord.Interaction):
        summoner_name = self.children[0].value
        summoner = Summoner(summoner_name)

        file = discord.File(summoner.getSummonerIconURL(),
                            filename=f"{summoner.icon_id}.png")
        embed = discord.Embed(title=interaction.user.name,
                              description="Please change your profile icon in the League of Legends client to the following to validate your account.")
        embed.set_image(url=f"attachment://{summoner.icon_id}.png")
        await interaction.response.send_message(file=file, embed=embed, ephemeral=True)

        while not summoner.validateSummoner():
            if summoner.timer > 0:
                summoner.timer -= 2
                await asyncio.sleep(2)
            else:
                await interaction.followup.send("Failed to validate your account in time. Please try again!", ephemeral=True)
                return

        avg, err = summoner.getSummonerMMR()
        rank = summoner.rank

        self.summoner_name = summoner_name
        self.elo = avg
        self.rank = rank

        self.stop()
