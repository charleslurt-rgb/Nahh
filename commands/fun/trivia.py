import discord
from discord import app_commands
from discord.ext import commands


class TriviaCommand(commands.Cog):
    """Command module for Play trivia."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="trivia")
    async def cmd_trivia_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`trivia` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="trivia", description="Play trivia.")
    async def cmd_trivia_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/trivia` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TriviaCommand(bot))
