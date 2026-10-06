import discord
from discord import app_commands
from discord.ext import commands


class RolesCommand(commands.Cog):
    """Command module for List server roles."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="info-roles")
    async def cmd_roles_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`roles` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="info-roles", description="List server roles.")
    async def cmd_roles_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/roles` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RolesCommand(bot))
