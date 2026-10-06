import discord
from discord import app_commands
from discord.ext import commands


class RemindCommand(commands.Cog):
    """Command module for Create a reminder."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="remind")
    async def cmd_remind_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`remind` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="remind", description="Create a reminder.")
    async def cmd_remind_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/remind` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RemindCommand(bot))
