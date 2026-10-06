import discord
from discord import app_commands
from discord.ext import commands


class PurgeCommand(commands.Cog):
    """Command module for Bulk delete messages."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="purge")
    async def cmd_purge_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`purge` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="purge", description="Bulk delete messages.")
    async def cmd_purge_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/purge` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PurgeCommand(bot))
