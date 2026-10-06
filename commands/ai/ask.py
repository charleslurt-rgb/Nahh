import discord
from discord import app_commands
from discord.ext import commands


class AskCommand(commands.Cog):
    """Command module for Ask the AI a question."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ask")
    async def cmd_ask_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`ask` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="ask", description="Ask the AI a question.")
    async def cmd_ask_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/ask` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AskCommand(bot))
