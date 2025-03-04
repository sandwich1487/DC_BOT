import discord
import json

with open(r"EveryoneBot\setting.json", mode="r", encoding="utf8") as jfile:
    settings = json.load(jfile)

intents = discord.Intents.all()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_message(message: discord.Message):
    if message.author == client.user:
        return
    
    prefix = "/"
    if message.content.startswith(prefix + "on"):
        settings["repeat"] = "True"
        with open(r"EveryoneBot\setting.json", mode="w", encoding="utf8") as jfile:
            json.dump(settings, jfile)
            await message.reply("@everyone 啟動!!!!!")
        return
    elif message.content.startswith(prefix + "off"):
        settings["repeat"] = "False"
        with open(r"EveryoneBot\setting.json", mode="w", encoding="utf8") as jfile:
            bye = discord.File(r"EveryoneBot\images\掰掰.JPG")
            json.dump(settings, jfile)
            await message.reply(file=bye)
        return
    
    if settings["repeat"] == "True":
        content = message.content
        await message.channel.send(f"@everyone\n{content}")
        
        images = message.attachments
        for img in images:
            file = await img.to_file(filename="image.png")
            await message.channel.send(file=file)
    

if __name__ == "__main__":
    client.run(settings["token"])