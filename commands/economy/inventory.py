import discord
from discord import app_commands
from discord.ext import commands


class InventoryCommand(commands.Cog):
    """Command module for View your inventory."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="inventory")
    async def cmd_inventory_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`inventory` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="inventory", description="View your inventory.")
    async def cmd_inventory_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/inventory` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(InventoryCommand(bot))
