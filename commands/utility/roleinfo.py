import discord
from discord import app_commands
from discord.ext import commands


class RoleinfoCommand(commands.Cog):
    """Command module for Show role information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="roleinfo")
    async def cmd_roleinfo_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`roleinfo` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="roleinfo", description="Show role information.")
    async def cmd_roleinfo_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/roleinfo` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RoleinfoCommand(bot))
