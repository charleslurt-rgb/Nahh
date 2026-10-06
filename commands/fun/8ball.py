import discord
from discord import app_commands
from discord.ext import commands


class 8ballCommand(commands.Cog):
    """Command module for Ask the magic 8-ball."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="8ball")
    async def cmd_8ball_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`8ball` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="8ball", description="Ask the magic 8-ball.")
    async def cmd_8ball_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/8ball` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(8ballCommand(bot))
