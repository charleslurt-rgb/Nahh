import discord
from discord import app_commands
from discord.ext import commands


class SettingsCommand(commands.Cog):
    """Command module for View server settings."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="settings")
    async def cmd_settings_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`settings` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="settings", description="View server settings.")
    async def cmd_settings_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/settings` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SettingsCommand(bot))
