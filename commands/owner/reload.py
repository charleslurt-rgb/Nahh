import discord
from discord import app_commands
from discord.ext import commands


class ReloadCommand(commands.Cog):
    """Command module for Reload a command module."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="reload")
    async def cmd_reload_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`reload` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="reload", description="Reload a command module.")
    async def cmd_reload_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/reload` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReloadCommand(bot))
