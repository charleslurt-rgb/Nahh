import discord
from discord import app_commands
from discord.ext import commands


class LogsCommand(commands.Cog):
    """Command module for Configure server logs."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="logs")
    async def cmd_logs_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`logs` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="logs", description="Configure server logs.")
    async def cmd_logs_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/logs` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LogsCommand(bot))
