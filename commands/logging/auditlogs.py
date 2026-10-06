import discord
from discord import app_commands
from discord.ext import commands


class AuditlogsCommand(commands.Cog):
    """Command module for View audit log information."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="auditlogs")
    async def cmd_auditlogs_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`auditlogs` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="auditlogs", description="View audit log information.")
    async def cmd_auditlogs_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/auditlogs` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(AuditlogsCommand(bot))
