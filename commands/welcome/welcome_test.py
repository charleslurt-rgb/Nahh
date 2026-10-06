import discord
from discord import app_commands
from discord.ext import commands


class WelcomeTestCommand(commands.Cog):
    """Command module for Test a welcome message."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="welcome-test")
    async def cmd_welcome_test_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`welcome-test` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="welcome-test", description="Test a welcome message.")
    async def cmd_welcome_test_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/welcome-test` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WelcomeTestCommand(bot))
