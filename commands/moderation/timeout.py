import discord
from discord import app_commands
from discord.ext import commands


class TimeoutCommand(commands.Cog):
    """Command module for Timeout a member."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="timeout")
    async def cmd_timeout_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`timeout` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="timeout", description="Timeout a member.")
    async def cmd_timeout_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/timeout` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TimeoutCommand(bot))
