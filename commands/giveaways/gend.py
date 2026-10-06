import discord
from discord import app_commands
from discord.ext import commands


class GendCommand(commands.Cog):
    """Command module for End a giveaway."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="gend")
    async def cmd_gend_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`gend` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="gend", description="End a giveaway.")
    async def cmd_gend_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/gend` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GendCommand(bot))
