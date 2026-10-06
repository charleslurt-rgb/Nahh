import discord
from discord import app_commands
from discord.ext import commands


class QuoteCommand(commands.Cog):
    """Command module for Show a random quote."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="quote")
    async def cmd_quote_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`quote` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="quote", description="Show a random quote.")
    async def cmd_quote_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/quote` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(QuoteCommand(bot))
