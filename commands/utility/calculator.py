import discord
from discord import app_commands
from discord.ext import commands


class CalculatorCommand(commands.Cog):
    """Command module for Calculate an expression."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="calculator")
    async def cmd_calculator_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`calculator` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="calculator", description="Calculate an expression.")
    async def cmd_calculator_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/calculator` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CalculatorCommand(bot))
