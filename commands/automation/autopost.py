import discord
from discord import app_commands
from discord.ext import commands


class AutopostCommand(commands.Cog):
    """Command module for Configure automatic posting."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="autopost")
    async def cmd_autopost_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`autopost` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="autopost", description="Configure automatic posting.")
    async def cmd_autopost_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/autopost` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutopostCommand(bot))
