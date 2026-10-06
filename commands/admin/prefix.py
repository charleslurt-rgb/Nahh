import discord
from discord import app_commands
from discord.ext import commands


class PrefixCommand(commands.Cog):
    """Command module for Change the server prefix."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="prefix")
    async def cmd_prefix_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`prefix` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="prefix", description="Change the server prefix.")
    async def cmd_prefix_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/prefix` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PrefixCommand(bot))
