import discord
from discord import app_commands
from discord.ext import commands


class DepositCommand(commands.Cog):
    """Command module for Deposit currency."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="deposit")
    async def cmd_deposit_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`deposit` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="deposit", description="Deposit currency.")
    async def cmd_deposit_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/deposit` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DepositCommand(bot))
