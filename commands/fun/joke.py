import discord
from discord import app_commands
from discord.ext import commands


class JokeCommand(commands.Cog):
    """Command module for Tell a joke."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="joke")
    async def cmd_joke_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`joke` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="joke", description="Tell a joke.")
    async def cmd_joke_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/joke` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(JokeCommand(bot))
