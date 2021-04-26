import os
import discord
import requests
import json
from web_server import keep_doge_alive

client = discord.Client()


def get_value():
    response = requests.get(
        "https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=cad"
    )
    #print(response.text)
    json_data = json.loads(response.text)
    dogeV = json_data['dogecoin']['cad']
    return (dogeV)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('^hello'):
        await message.channel.send('Much Hello! Such Wow!')

    if 'snoz' in message.content:
        await message.channel.send('Much Snoz! Such Length!')

    if 'dodge' in message.content or 'doge' in message.content:
        dv = get_value()
        returnMessage = "Doge coin is currently at: {dogeV:.4} CAD".format(
            dogeV=dv)
        await message.channel.send(returnMessage)



keep_doge_alive()
client.run(os.environ['discordCode'])
