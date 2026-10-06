import discord
from discord import app_commands
from discord.ext import commands


class EventsCommand(commands.Cog):
    """Command module for Configure event notifications."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="auto-events")
    async def cmd_events_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`events` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="auto-events", description="Configure event notifications.")
    async def cmd_events_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/events` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EventsCommand(bot))
