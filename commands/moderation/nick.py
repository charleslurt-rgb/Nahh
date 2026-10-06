import discord
from discord import app_commands
from discord.ext import commands


class NickCommand(commands.Cog):
    """Command module for Change a member nickname."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="nick")
    async def cmd_nick_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`nick` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="nick", description="Change a member nickname.")
    async def cmd_nick_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/nick` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(NickCommand(bot))
