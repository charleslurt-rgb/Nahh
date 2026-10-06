import discord
from discord import app_commands
from discord.ext import commands


class GuessCommand(commands.Cog):
    """Command module for Play a guessing game."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="guess")
    async def cmd_guess_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`guess` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="guess", description="Play a guessing game.")
    async def cmd_guess_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/guess` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuessCommand(bot))
