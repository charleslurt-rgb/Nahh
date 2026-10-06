import discord
from discord import app_commands
from discord.ext import commands


class StatusCommand(commands.Cog):
    """Command module for Show bot status."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="info-status")
    async def cmd_status_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`status` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="info-status", description="Show bot status.")
    async def cmd_status_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/status` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StatusCommand(bot))
