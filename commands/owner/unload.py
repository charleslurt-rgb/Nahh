import discord
from discord import app_commands
from discord.ext import commands


class UnloadCommand(commands.Cog):
    """Command module for Unload a command module."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="unload")
    async def cmd_unload_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`unload` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="unload", description="Unload a command module.")
    async def cmd_unload_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/unload` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UnloadCommand(bot))
