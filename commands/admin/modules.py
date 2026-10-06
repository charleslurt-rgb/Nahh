import discord
from discord import app_commands
from discord.ext import commands


class ModulesCommand(commands.Cog):
    """Command module for Enable or disable bot modules."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="modules")
    async def cmd_modules_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`modules` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="modules", description="Enable or disable bot modules.")
    async def cmd_modules_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/modules` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ModulesCommand(bot))
