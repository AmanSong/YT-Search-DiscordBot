import discord
import urllib.request
import re
from webserver import keep_alive
import os

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

#function for searching youtube videos
@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = message.content.lower()

    #stop bot from replying to itself infinitely
    if message.author == client.user:
        return

    if user_message.startswith("!search"):
        #get the title of the video
        video = str(user_message).split(' ', 1)
        remove = video.pop(0)
        video = ' '.join(map(str, video))
        video = video.replace(' ', '+')

        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + video)
        video_id = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        await message.channel.send("https://www.youtube.com/watch?v=" + video_id[0])

keep_alive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)