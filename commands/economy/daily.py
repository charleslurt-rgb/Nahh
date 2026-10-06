import discord
from discord import app_commands
from discord.ext import commands


class DailyCommand(commands.Cog):
    """Command module for Claim daily currency."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="daily")
    async def cmd_daily_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`daily` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="daily", description="Claim daily currency.")
    async def cmd_daily_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/daily` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DailyCommand(bot))
