import discord
from discord.ui import InputText, Modal

class SummonerModal(Modal):
    def __init__(self) -> None:
        super().__init__("Summoner registration Modal")
        self.add_item(InputText(label="Summoner name"), placeholder="Your summoner name")
        
    async def callback(self, interaction: discord.Interaction):
        """Callback function for the modal.

        Args:
            interaction (discord.Interaction): Interaction that triggers the modal
        """        
        await interaction.response.send_message("f{self.children[0].value}")