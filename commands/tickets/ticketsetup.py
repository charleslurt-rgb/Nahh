import discord
from discord import app_commands
from discord.ext import commands


class TicketsetupCommand(commands.Cog):
    """Command module for Configure the ticket system."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ticketsetup")
    async def cmd_ticketsetup_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`ticketsetup` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="ticketsetup", description="Configure the ticket system.")
    async def cmd_ticketsetup_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/ticketsetup` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TicketsetupCommand(bot))
