import discord
from discord import app_commands
from discord.ext import commands


class MessageLogsCommand(commands.Cog):
    """Command module for Configure message logs."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="message-logs")
    async def cmd_message_logs_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`message-logs` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="message-logs", description="Configure message logs.")
    async def cmd_message_logs_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/message-logs` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MessageLogsCommand(bot))
