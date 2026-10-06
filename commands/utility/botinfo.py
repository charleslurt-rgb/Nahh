import discord
from discord import app_commands
from discord.ext import commands


class BotinfoCommand(commands.Cog):
    """Command module for Show bot information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="botinfo")
    async def cmd_botinfo_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`botinfo` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="botinfo", description="Show bot information.")
    async def cmd_botinfo_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/botinfo` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(BotinfoCommand(bot))
