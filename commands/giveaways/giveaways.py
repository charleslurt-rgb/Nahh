import discord
from discord import app_commands
from discord.ext import commands


class GiveawaysCommand(commands.Cog):
    """Command module for List active giveaways."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="giveaways")
    async def cmd_giveaways_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`giveaways` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="giveaways", description="List active giveaways.")
    async def cmd_giveaways_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/giveaways` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(GiveawaysCommand(bot))
