import discord
from discord import app_commands
from discord.ext import commands


class StarboardCommand(commands.Cog):
    """Command module for Configure a starboard."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="starboard")
    async def cmd_starboard_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`starboard` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="starboard", description="Configure a starboard.")
    async def cmd_starboard_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/starboard` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(StarboardCommand(bot))
