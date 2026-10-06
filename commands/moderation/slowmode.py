import discord
from discord import app_commands
from discord.ext import commands


class SlowmodeCommand(commands.Cog):
    """Command module for Configure channel slowmode."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="slowmode")
    async def cmd_slowmode_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`slowmode` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="slowmode", description="Configure channel slowmode.")
    async def cmd_slowmode_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/slowmode` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SlowmodeCommand(bot))
