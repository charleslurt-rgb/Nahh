import discord
from discord import app_commands
from discord.ext import commands


class RoleCommand(commands.Cog):
    """Command module for Manage a member's roles."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="role")
    async def cmd_role_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`role` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="role", description="Manage a member's roles.")
    async def cmd_role_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/role` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(RoleCommand(bot))
