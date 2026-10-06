import discord
from discord import app_commands
from discord.ext import commands


class BuyCommand(commands.Cog):
    """Command module for Buy an item."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="buy")
    async def cmd_buy_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`buy` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="buy", description="Buy an item.")
    async def cmd_buy_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/buy` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BuyCommand(bot))
