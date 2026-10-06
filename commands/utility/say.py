import discord
from discord import app_commands
from discord.ext import commands


class SayCommand(commands.Cog):
    """Command module for Make the bot send a message."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="say")
    async def cmd_say_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`say` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="say", description="Make the bot send a message.")
    async def cmd_say_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/say` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SayCommand(bot))
