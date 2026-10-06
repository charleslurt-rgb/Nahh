import discord
from discord import app_commands
from discord.ext import commands


class ImagineCommand(commands.Cog):
    """Command module for Generate an image prompt."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="imagine")
    async def cmd_imagine_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`imagine` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="imagine", description="Generate an image prompt.")
    async def cmd_imagine_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/imagine` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ImagineCommand(bot))
