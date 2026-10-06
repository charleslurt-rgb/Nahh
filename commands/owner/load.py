import discord
from discord import app_commands
from discord.ext import commands


class LoadCommand(commands.Cog):
    """Command module for Load a command module."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="load")
    async def cmd_load_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`load` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="load", description="Load a command module.")
    async def cmd_load_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/load` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LoadCommand(bot))
