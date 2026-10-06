import discord
from discord import app_commands
from discord.ext import commands


class AvatarCommand(commands.Cog):
    """Command module for Show a user's avatar."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="avatar")
    async def cmd_avatar_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`avatar` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="avatar", description="Show a user's avatar.")
    async def cmd_avatar_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/avatar` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AvatarCommand(bot))
