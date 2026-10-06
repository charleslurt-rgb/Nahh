import discord
from discord import app_commands
from discord.ext import commands


class ReactionrolesCommand(commands.Cog):
    """Command module for Configure reaction or button roles."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="reactionroles")
    async def cmd_reactionroles_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`reactionroles` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="reactionroles", description="Configure reaction or button roles.")
    async def cmd_reactionroles_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/reactionroles` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ReactionrolesCommand(bot))
