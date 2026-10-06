import discord
from discord import app_commands
from discord.ext import commands


class ChooseCommand(commands.Cog):
    """Command module for Choose an option."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="fun-choose")
    async def cmd_choose_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`choose` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="fun-choose", description="Choose an option.")
    async def cmd_choose_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/choose` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChooseCommand(bot))
