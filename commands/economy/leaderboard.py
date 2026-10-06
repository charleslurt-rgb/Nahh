import discord
from discord import app_commands
from discord.ext import commands


class LeaderboardCommand(commands.Cog):
    """Command module for View the economy leaderboard."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="leaderboard")
    async def cmd_leaderboard_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`leaderboard` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="leaderboard", description="View the economy leaderboard.")
    async def cmd_leaderboard_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/leaderboard` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LeaderboardCommand(bot))
