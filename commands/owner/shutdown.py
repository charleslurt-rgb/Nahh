import discord
from discord import app_commands
from discord.ext import commands


class ShutdownCommand(commands.Cog):
    """Command module for Shut down the bot."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="shutdown")
    async def cmd_shutdown_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`shutdown` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="shutdown", description="Shut down the bot.")
    async def cmd_shutdown_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/shutdown` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ShutdownCommand(bot))
