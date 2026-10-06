import discord
from discord import app_commands
from discord.ext import commands


class SyncCommand(commands.Cog):
    """Command module for Sync application commands."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="sync")
    async def cmd_sync_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`sync` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="sync", description="Sync application commands.")
    async def cmd_sync_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/sync` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SyncCommand(bot))
