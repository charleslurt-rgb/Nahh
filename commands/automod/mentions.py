import discord
from discord import app_commands
from discord.ext import commands


class MentionsCommand(commands.Cog):
    """Command module for Configure mention protection."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="mentions")
    async def cmd_mentions_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`mentions` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="mentions", description="Configure mention protection.")
    async def cmd_mentions_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/mentions` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(MentionsCommand(bot))
