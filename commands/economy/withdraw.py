import discord
from discord import app_commands
from discord.ext import commands


class WithdrawCommand(commands.Cog):
    """Command module for Withdraw currency."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="withdraw")
    async def cmd_withdraw_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`withdraw` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="withdraw", description="Withdraw currency.")
    async def cmd_withdraw_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/withdraw` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WithdrawCommand(bot))
