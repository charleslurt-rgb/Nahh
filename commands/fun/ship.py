import discord
from discord import app_commands
from discord.ext import commands


class ShipCommand(commands.Cog):
    """Command module for Get a fictional compatibility score."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ship")
    async def cmd_ship_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`ship` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="ship", description="Get a fictional compatibility score.")
    async def cmd_ship_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/ship` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ShipCommand(bot))
