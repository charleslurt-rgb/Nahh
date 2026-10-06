import discord
from discord import app_commands
from discord.ext import commands


class SummarizeCommand(commands.Cog):
    """Command module for Summarize text."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="summarize")
    async def cmd_summarize_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`summarize` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="summarize", description="Summarize text.")
    async def cmd_summarize_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/summarize` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SummarizeCommand(bot))
