import discord
from discord import app_commands
from discord.ext import commands


class AutoresponderCommand(commands.Cog):
    """Command module for Configure automatic responses."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="autoresponder")
    async def cmd_autoresponder_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`autoresponder` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="autoresponder", description="Configure automatic responses.")
    async def cmd_autoresponder_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/autoresponder` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AutoresponderCommand(bot))
