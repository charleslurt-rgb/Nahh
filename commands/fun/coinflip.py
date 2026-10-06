import discord
from discord import app_commands
from discord.ext import commands


class CoinflipCommand(commands.Cog):
    """Command module for Flip a coin."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="coinflip")
    async def cmd_coinflip_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`coinflip` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="coinflip", description="Flip a coin.")
    async def cmd_coinflip_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/coinflip` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CoinflipCommand(bot))
