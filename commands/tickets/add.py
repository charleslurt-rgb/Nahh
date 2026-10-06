import discord
from discord import app_commands
from discord.ext import commands


class AddCommand(commands.Cog):
    """Command module for Add a user to a ticket."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="add")
    async def cmd_add_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`add` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="add", description="Add a user to a ticket.")
    async def cmd_add_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/add` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AddCommand(bot))
