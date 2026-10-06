import discord
from discord import app_commands
from discord.ext import commands


class EmbedCommand(commands.Cog):
    """Command module for Create an embed."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="embed")
    async def cmd_embed_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`embed` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="embed", description="Create an embed.")
    async def cmd_embed_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/embed` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(EmbedCommand(bot))
