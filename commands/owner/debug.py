import discord
from discord import app_commands
from discord.ext import commands


class DebugCommand(commands.Cog):
    """Command module for Show developer diagnostics."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="debug")
    async def cmd_debug_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`debug` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="debug", description="Show developer diagnostics.")
    async def cmd_debug_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/debug` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(DebugCommand(bot))
