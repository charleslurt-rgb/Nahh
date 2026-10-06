import discord
from discord import app_commands
from discord.ext import commands


class GuildsCommand(commands.Cog):
    """Command module for List bot guilds."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="guilds")
    async def cmd_guilds_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`guilds` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="guilds", description="List bot guilds.")
    async def cmd_guilds_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/guilds` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GuildsCommand(bot))
