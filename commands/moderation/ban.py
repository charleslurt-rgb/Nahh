import discord
from discord import app_commands
from discord.ext import commands


class BanCommand(commands.Cog):
    """Command module for Ban a member."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ban")
    async def cmd_ban_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`ban` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="ban", description="Ban a member.")
    async def cmd_ban_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/ban` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BanCommand(bot))
