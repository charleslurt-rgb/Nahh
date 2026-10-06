import discord
from discord import app_commands
from discord.ext import commands


class CapsCommand(commands.Cog):
    """Command module for Configure excessive-capital filtering."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="caps")
    async def cmd_caps_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`caps` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="caps", description="Configure excessive-capital filtering.")
    async def cmd_caps_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/caps` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(CapsCommand(bot))
