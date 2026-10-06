import discord
from discord import app_commands
from discord.ext import commands


class MemeCommand(commands.Cog):
    """Command module for Show a meme."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="meme")
    async def cmd_meme_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`meme` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="meme", description="Show a meme.")
    async def cmd_meme_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/meme` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MemeCommand(bot))
