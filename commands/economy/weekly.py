import discord
from discord import app_commands
from discord.ext import commands


class WeeklyCommand(commands.Cog):
    """Command module for Claim weekly currency."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="weekly")
    async def cmd_weekly_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`weekly` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="weekly", description="Claim weekly currency.")
    async def cmd_weekly_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/weekly` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WeeklyCommand(bot))
