import discord
from discord import app_commands
from discord.ext import commands


class InviteCommand(commands.Cog):
    """Command module for Show the bot invite."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="invite")
    async def cmd_invite_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`invite` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="invite", description="Show the bot invite.")
    async def cmd_invite_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/invite` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InviteCommand(bot))
