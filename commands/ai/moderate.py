import discord
from discord import app_commands
from discord.ext import commands


class ModerateCommand(commands.Cog):
    """Command module for Analyze content for moderation."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="moderate")
    async def cmd_moderate_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`moderate` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="moderate", description="Analyze content for moderation.")
    async def cmd_moderate_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/moderate` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModerateCommand(bot))
