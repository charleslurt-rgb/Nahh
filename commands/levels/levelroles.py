import discord
from discord import app_commands
from discord.ext import commands


class LevelrolesCommand(commands.Cog):
    """Command module for Configure level roles."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="levelroles")
    async def cmd_levelroles_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`levelroles` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="levelroles", description="Configure level roles.")
    async def cmd_levelroles_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/levelroles` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(LevelrolesCommand(bot))
