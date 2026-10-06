import discord
from discord import app_commands
from discord.ext import commands


class ScheduleCommand(commands.Cog):
    """Command module for Schedule a message."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="schedule")
    async def cmd_schedule_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`schedule` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="schedule", description="Schedule a message.")
    async def cmd_schedule_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/schedule` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ScheduleCommand(bot))
