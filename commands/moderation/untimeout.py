import discord
from discord import app_commands
from discord.ext import commands


class UntimeoutCommand(commands.Cog):
    """Command module for Remove a timeout."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="untimeout")
    async def cmd_untimeout_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`untimeout` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="untimeout", description="Remove a timeout.")
    async def cmd_untimeout_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/untimeout` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UntimeoutCommand(bot))
