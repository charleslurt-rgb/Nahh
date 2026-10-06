import discord
from discord import app_commands
from discord.ext import commands


class StickyCommand(commands.Cog):
    """Command module for Configure sticky messages."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="sticky")
    async def cmd_sticky_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`sticky` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="sticky", description="Configure sticky messages.")
    async def cmd_sticky_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/sticky` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StickyCommand(bot))
