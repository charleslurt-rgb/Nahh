import discord
from discord import app_commands
from discord.ext import commands


class AntispamCommand(commands.Cog):
    """Command module for Configure anti-spam."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="antispam")
    async def cmd_antispam_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`antispam` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="antispam", description="Configure anti-spam.")
    async def cmd_antispam_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/antispam` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AntispamCommand(bot))
