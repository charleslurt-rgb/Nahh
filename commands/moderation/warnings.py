import discord
from discord import app_commands
from discord.ext import commands


class WarningsCommand(commands.Cog):
    """Command module for View member warnings."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="warnings")
    async def cmd_warnings_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`warnings` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="warnings", description="View member warnings.")
    async def cmd_warnings_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/warnings` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WarningsCommand(bot))
