import discord
from discord import app_commands
from discord.ext import commands


class WorkCommand(commands.Cog):
    """Command module for Work for currency."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="work")
    async def cmd_work_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`work` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="work", description="Work for currency.")
    async def cmd_work_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/work` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(WorkCommand(bot))
