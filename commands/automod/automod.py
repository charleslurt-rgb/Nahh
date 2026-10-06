import discord
from discord import app_commands
from discord.ext import commands


class AutomodCommand(commands.Cog):
    """Command module for Configure automatic moderation."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="automod")
    async def cmd_automod_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`automod` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="automod", description="Configure automatic moderation.")
    async def cmd_automod_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/automod` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutomodCommand(bot))
