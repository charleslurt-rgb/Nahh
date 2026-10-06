import discord
from discord import app_commands
from discord.ext import commands


class TranslateCommand(commands.Cog):
    """Command module for Translate text."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="translate")
    async def cmd_translate_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`translate` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="translate", description="Translate text.")
    async def cmd_translate_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/translate` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TranslateCommand(bot))
