import discord
from discord import app_commands
from discord.ext import commands


class UnlockCommand(commands.Cog):
    """Command module for Unlock a channel."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="unlock")
    async def cmd_unlock_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`unlock` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="unlock", description="Unlock a channel.")
    async def cmd_unlock_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/unlock` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UnlockCommand(bot))
