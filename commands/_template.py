# Copy this file into a category directory when creating a new command.
# Replace the class name, command names, descriptions, and implementation.

import discord
from discord import app_commands
from discord.ext import commands


class Example(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="example")
    async def example_prefix(self, ctx: commands.Context) -> None:
        await ctx.send("Example prefix command.")

    @app_commands.command(name="example", description="Example slash command.")
    async def example_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Example slash command.")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Example(bot))
