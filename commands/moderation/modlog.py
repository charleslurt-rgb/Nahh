import discord
from discord import app_commands
from discord.ext import commands


class ModlogCommand(commands.Cog):
    """Command module for Configure moderation logs."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="modlog")
    async def cmd_modlog_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`modlog` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="modlog", description="Configure moderation logs.")
    async def cmd_modlog_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/modlog` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModlogCommand(bot))
