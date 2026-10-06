import discord
from discord import app_commands
from discord.ext import commands


class TicketCommand(commands.Cog):
    """Command module for Create a support ticket."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="ticket")
    async def cmd_ticket_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`ticket` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="ticket", description="Create a support ticket.")
    async def cmd_ticket_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/ticket` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(TicketCommand(bot))
