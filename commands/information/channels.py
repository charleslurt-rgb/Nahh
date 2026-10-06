import discord
from discord import app_commands
from discord.ext import commands


class ChannelsCommand(commands.Cog):
    """Command module for List server channels."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="channels")
    async def cmd_channels_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`channels` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="channels", description="List server channels.")
    async def cmd_channels_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/channels` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChannelsCommand(bot))
