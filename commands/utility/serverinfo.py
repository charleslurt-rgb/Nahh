import discord
from discord import app_commands
from discord.ext import commands


class ServerinfoCommand(commands.Cog):
    """Command module for Show server information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="serverinfo")
    async def cmd_serverinfo_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`serverinfo` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="serverinfo", description="Show server information.")
    async def cmd_serverinfo_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/serverinfo` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ServerinfoCommand(bot))
