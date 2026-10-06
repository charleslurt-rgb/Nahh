import discord
from discord import app_commands
from discord.ext import commands


class AliasesCommand(commands.Cog):
    """Command module for Manage command aliases."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="aliases")
    async def cmd_aliases_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`aliases` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="aliases", description="Manage command aliases.")
    async def cmd_aliases_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/aliases` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AliasesCommand(bot))
