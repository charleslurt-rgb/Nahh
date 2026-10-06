import discord
from discord import app_commands
from discord.ext import commands


class SoftbanCommand(commands.Cog):
    """Command module for Ban and unban a member to clear messages."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="softban")
    async def cmd_softban_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`softban` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="softban", description="Ban and unban a member to clear messages.")
    async def cmd_softban_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/softban` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(SoftbanCommand(bot))
