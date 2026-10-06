import discord
from discord import app_commands
from discord.ext import commands


class WelcomeCommand(commands.Cog):
    """Command module for Configure welcome messages."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="admin-welcome")
    async def cmd_welcome_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`welcome` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="admin-welcome", description="Configure welcome messages.")
    async def cmd_welcome_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/welcome` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WelcomeCommand(bot))
