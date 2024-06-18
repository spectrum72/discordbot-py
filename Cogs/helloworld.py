import discord
from discord.ext import commands
from discord import app_commands

class Helloworld(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="테스트", description="헬로우월드")
    async def helloworld(self, interaction: discord.Interaction):
        await interaction.response.send_message(content="Hello world")

async def setup(bot: commands.Bot):
    await bot.add_cog(Helloworld(bot))