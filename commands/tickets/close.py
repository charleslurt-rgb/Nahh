import discord
from discord import app_commands
from discord.ext import commands


class CloseCommand(commands.Cog):
    """Command module for Close a ticket."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="close")
    async def cmd_close_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`close` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="close", description="Close a ticket.")
    async def cmd_close_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/close` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CloseCommand(bot))
