import discord
from discord import app_commands
from discord.ext import commands


class KickCommand(commands.Cog):
    """Command module for Kick a member."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="kick")
    async def cmd_kick_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`kick` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="kick", description="Kick a member.")
    async def cmd_kick_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/kick` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(KickCommand(bot))
