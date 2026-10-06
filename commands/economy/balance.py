import discord
from discord import app_commands
from discord.ext import commands


class BalanceCommand(commands.Cog):
    """Command module for View your balance."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="balance")
    async def cmd_balance_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`balance` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="balance", description="View your balance.")
    async def cmd_balance_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/balance` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BalanceCommand(bot))
