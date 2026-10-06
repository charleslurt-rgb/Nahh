import discord
from discord import app_commands
from discord.ext import commands


class LevelCommand(commands.Cog):
    """Command module for View your level."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="level")
    async def cmd_level_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`level` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="level", description="View your level.")
    async def cmd_level_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/level` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LevelCommand(bot))
