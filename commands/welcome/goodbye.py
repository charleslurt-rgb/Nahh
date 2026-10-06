import discord
from discord import app_commands
from discord.ext import commands


class GoodbyeCommand(commands.Cog):
    """Command module for Configure goodbye messages."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="goodbye")
    async def cmd_goodbye_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`goodbye` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="goodbye", description="Configure goodbye messages.")
    async def cmd_goodbye_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/goodbye` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GoodbyeCommand(bot))
