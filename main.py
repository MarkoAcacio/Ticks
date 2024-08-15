import connect
import errors
import discord
from discord.ext import commands
from discord import app_commands
import discord.interactions
from discord.ui import Button, View

TOKEN = connect.TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='.', intents=intents)

#Output if the client is successfully run
@bot.event
async def on_ready() -> None:
    print("Bot Started")
    try:
        synced = await bot.tree.sync()
        print(f"Bot Synced {len(synced)} commands.")
    except Exception as e:
        print(e)

@bot.tree.command(name="setupticket")
@app_commands.describe(text="Ticket Display Text. ", btntxt="Ticket Button Text.")
async def setupticket(interaction: discord.Interaction, text:str, btntxt:str): 
    btn = Button(style=discord.ButtonStyle.secondary, label=btntxt, custom_id="btn1")
    view = View()
    view.add_item(btn)
    
    await interaction.response.send_message(f"Channel Setup Succesfull.", ephemeral = True)
    await interaction.channel.send(f"{text}", view=view)

@bot.tree.command(name="purge")
@app_commands.describe(num= "Number of Text to delete.")
async def purge(interaction: discord.Interaction, num:int):
    delete = await interaction.channel.purge(limit=num)

    await interaction.response.send_message(f"Deleted {len(delete)} messages.", ephemeral=True)
    


#main returns none / is not expecting any value
def main() -> None:
    #runs the bot with out token
    bot.run(TOKEN)

if __name__ == '__main__':
    main()
