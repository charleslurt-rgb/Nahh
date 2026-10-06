import discord
from discord import app_commands
from discord.ext import commands


class GoodbyeTestCommand(commands.Cog):
    """Command module for Test a goodbye message."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="goodbye-test")
    async def cmd_goodbye_test_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`goodbye-test` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="goodbye-test", description="Test a goodbye message.")
    async def cmd_goodbye_test_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/goodbye-test` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GoodbyeTestCommand(bot))
