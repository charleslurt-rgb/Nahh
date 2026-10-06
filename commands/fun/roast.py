import discord
from discord import app_commands
from discord.ext import commands


class RoastCommand(commands.Cog):
    """Command module for Generate a playful roast."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="roast")
    async def cmd_roast_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`roast` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="roast", description="Generate a playful roast.")
    async def cmd_roast_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/roast` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RoastCommand(bot))
