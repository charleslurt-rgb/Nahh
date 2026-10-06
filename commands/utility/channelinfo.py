import discord
from discord import app_commands
from discord.ext import commands


class ChannelinfoCommand(commands.Cog):
    """Command module for Show channel information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="channelinfo")
    async def cmd_channelinfo_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`channelinfo` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="channelinfo", description="Show channel information.")
    async def cmd_channelinfo_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/channelinfo` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChannelinfoCommand(bot))
