import main
import discord
from discord.ext import commands
from discord import app_commands
import discord.interactions


@main.purge.error
async def purge_error(interaction: discord.Interaction, error:app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("You do not have the permission to use this command.", ephemeral=True)
    else:
        await interaction.response.send_message("An error occured while running the command.", ephemeral=True)

@main.setupticket.error
async def setup_ticket_error(interaction: discord.Interaction, error:app_commands.AppCommandError):
    if isinstance(error,app_commands.MissingPermissions):
        await interaction.response.send_message("You do not have the permission to use this command.", ephemeral=True)
    else:
        await interaction.response.send_message("An error occured while running the command.", ephemeral=True)