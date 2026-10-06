import discord
from discord import app_commands
from discord.ext import commands


class ShopCommand(commands.Cog):
    """Command module for View the server shop."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="shop")
    async def cmd_shop_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`shop` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="shop", description="View the server shop.")
    async def cmd_shop_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/shop` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ShopCommand(bot))
