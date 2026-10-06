import discord
from discord import app_commands
from discord.ext import commands


class RpsCommand(commands.Cog):
    """Command module for Play rock paper scissors."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="rps")
    async def cmd_rps_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`rps` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="rps", description="Play rock paper scissors.")
    async def cmd_rps_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/rps` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RpsCommand(bot))
