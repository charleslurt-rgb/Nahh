import discord
from discord import app_commands
from discord.ext import commands


class UnbanCommand(commands.Cog):
    """Command module for Unban a user."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="unban")
    async def cmd_unban_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`unban` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="unban", description="Unban a user.")
    async def cmd_unban_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/unban` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UnbanCommand(bot))
