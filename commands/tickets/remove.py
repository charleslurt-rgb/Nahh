import discord
from discord import app_commands
from discord.ext import commands


class RemoveCommand(commands.Cog):
    """Command module for Remove a user from a ticket."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="remove")
    async def cmd_remove_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`remove` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="remove", description="Remove a user from a ticket.")
    async def cmd_remove_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/remove` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RemoveCommand(bot))
