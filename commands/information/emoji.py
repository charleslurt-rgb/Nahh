import discord
from discord import app_commands
from discord.ext import commands


class EmojiCommand(commands.Cog):
    """Command module for Show emoji information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="emoji")
    async def cmd_emoji_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`emoji` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="emoji", description="Show emoji information.")
    async def cmd_emoji_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/emoji` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EmojiCommand(bot))
