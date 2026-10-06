import discord
from discord import app_commands
from discord.ext import commands


class AntilinkCommand(commands.Cog):
    """Command module for Configure link filtering."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="antilink")
    async def cmd_antilink_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`antilink` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="antilink", description="Configure link filtering.")
    async def cmd_antilink_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/antilink` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AntilinkCommand(bot))
