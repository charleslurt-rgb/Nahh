import discord
from discord import app_commands
from discord.ext import commands


class ClearCommand(commands.Cog):
    """Command module for Delete messages."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="clear")
    async def cmd_clear_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`clear` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="clear", description="Delete messages.")
    async def cmd_clear_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/clear` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ClearCommand(bot))
