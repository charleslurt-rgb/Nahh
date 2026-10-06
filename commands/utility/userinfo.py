import discord
from discord import app_commands
from discord.ext import commands


class UserinfoCommand(commands.Cog):
    """Command module for Show user information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="userinfo")
    async def cmd_userinfo_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`userinfo` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="userinfo", description="Show user information.")
    async def cmd_userinfo_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/userinfo` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(UserinfoCommand(bot))
