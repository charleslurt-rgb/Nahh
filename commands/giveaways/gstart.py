import discord
from discord import app_commands
from discord.ext import commands


class GstartCommand(commands.Cog):
    """Command module for Start a giveaway."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="gstart")
    async def cmd_gstart_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`gstart` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="gstart", description="Start a giveaway.")
    async def cmd_gstart_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/gstart` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GstartCommand(bot))
