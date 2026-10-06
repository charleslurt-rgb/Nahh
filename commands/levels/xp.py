import discord
from discord import app_commands
from discord.ext import commands


class XpCommand(commands.Cog):
    """Command module for Manage XP settings."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="xp")
    async def cmd_xp_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`xp` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="xp", description="Manage XP settings.")
    async def cmd_xp_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/xp` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(XpCommand(bot))
