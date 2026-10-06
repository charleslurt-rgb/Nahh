import discord
from discord import app_commands
from discord.ext import commands


class AfkCommand(commands.Cog):
    """Command module for Set an AFK status."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="afk")
    async def cmd_afk_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`afk` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="afk", description="Set an AFK status.")
    async def cmd_afk_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/afk` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AfkCommand(bot))
