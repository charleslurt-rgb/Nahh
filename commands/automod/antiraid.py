import discord
from discord import app_commands
from discord.ext import commands


class AntiraidCommand(commands.Cog):
    """Command module for Configure anti-raid protection."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="antiraid")
    async def cmd_antiraid_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`antiraid` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="antiraid", description="Configure anti-raid protection.")
    async def cmd_antiraid_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/antiraid` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AntiraidCommand(bot))
