import discord
from discord import app_commands
from discord.ext import commands


class HelpCommand(commands.Cog):
    """Command module for Show bot help."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="help")
    async def cmd_help_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`help` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="help", description="Show bot help.")
    async def cmd_help_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/help` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(HelpCommand(bot))
