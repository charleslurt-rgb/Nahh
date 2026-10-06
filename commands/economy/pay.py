import discord
from discord import app_commands
from discord.ext import commands


class PayCommand(commands.Cog):
    """Command module for Pay another user."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="pay")
    async def cmd_pay_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`pay` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="pay", description="Pay another user.")
    async def cmd_pay_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/pay` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PayCommand(bot))
