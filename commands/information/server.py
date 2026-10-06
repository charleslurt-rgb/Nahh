import discord
from discord import app_commands
from discord.ext import commands


class ServerCommand(commands.Cog):
    """Command module for Show server information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="info-server")
    async def cmd_server_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`server` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="info-server", description="Show server information.")
    async def cmd_server_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/server` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ServerCommand(bot))
