import discord
from discord import app_commands
from discord.ext import commands


class BannerCommand(commands.Cog):
    """Command module for Show a user's banner."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="banner")
    async def cmd_banner_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`banner` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="banner", description="Show a user's banner.")
    async def cmd_banner_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/banner` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BannerCommand(bot))
