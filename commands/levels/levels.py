import discord
from discord import app_commands
from discord.ext import commands


class LevelsCommand(commands.Cog):
    """Command module for View the server level leaderboard."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="levels")
    async def cmd_levels_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`levels` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="levels", description="View the server level leaderboard.")
    async def cmd_levels_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/levels` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LevelsCommand(bot))
