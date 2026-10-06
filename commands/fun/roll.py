import discord
from discord import app_commands
from discord.ext import commands


class RollCommand(commands.Cog):
    """Command module for Roll dice."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="roll")
    async def cmd_roll_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`roll` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="roll", description="Roll dice.")
    async def cmd_roll_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/roll` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RollCommand(bot))
