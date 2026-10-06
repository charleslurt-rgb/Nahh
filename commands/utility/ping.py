import discord
from discord import app_commands
from discord.ext import commands


class PingCommand(commands.Cog):
    """Command module for Check bot latency."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ping")
    async def cmd_ping_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`ping` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="ping", description="Check bot latency.")
    async def cmd_ping_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/ping` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(PingCommand(bot))
