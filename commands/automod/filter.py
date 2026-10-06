import discord
from discord import app_commands
from discord.ext import commands


class FilterCommand(commands.Cog):
    """Command module for Configure word filtering."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="filter")
    async def cmd_filter_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`filter` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="filter", description="Configure word filtering.")
    async def cmd_filter_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/filter` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(FilterCommand(bot))
