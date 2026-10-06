import discord
from discord import app_commands
from discord.ext import commands


class EvalCommand(commands.Cog):
    """Command module for Developer-only evaluation command."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="eval")
    async def cmd_eval_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`eval` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="eval", description="Developer-only evaluation command.")
    async def cmd_eval_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/eval` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EvalCommand(bot))
