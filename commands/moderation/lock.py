import discord
from discord import app_commands
from discord.ext import commands


class LockCommand(commands.Cog):
    """Command module for Lock a channel."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="lock")
    async def cmd_lock_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`lock` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="lock", description="Lock a channel.")
    async def cmd_lock_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/lock` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LockCommand(bot))
