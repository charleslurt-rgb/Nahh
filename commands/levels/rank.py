import discord
from discord import app_commands
from discord.ext import commands


class RankCommand(commands.Cog):
    """Command module for View your rank."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="rank")
    async def cmd_rank_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`rank` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="rank", description="View your rank.")
    async def cmd_rank_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/rank` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RankCommand(bot))
