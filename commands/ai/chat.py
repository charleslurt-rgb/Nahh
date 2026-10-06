import discord
from discord import app_commands
from discord.ext import commands


class ChatCommand(commands.Cog):
    """Command module for Start an AI chat."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @commands.command(name="chat")
    async def cmd_chat_prefix(self, ctx: commands.Context) -> None:
        await ctx.send(
            f"`chat` is scaffolded and ready for implementation."
        )

    @app_commands.command(name="chat", description="Start an AI chat.")
    async def cmd_chat_slash(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(
            f"`/chat` is scaffolded and ready for implementation."
        )


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ChatCommand(bot))
