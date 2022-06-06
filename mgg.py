import discord
import randomGenreGenerator
import characterGenerator

env_vars = {}
with open('./.env') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)
        env_vars[key] = value

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('MGG -new-genre'):
        await message.channel.send(randomGenreGenerator.generator())
    #if message.content.startswith('-generate-character'):
    #    await message.channel.send(characterGenerator.generator())
    if message.content.startswith('MGG -help'):
        await message.channel.send('Metal Genre Generator Help\n\nNew random genre: MGG -new-genre\nHelp: MGG -help')
    
        

client.run(env_vars['TOKEN'])