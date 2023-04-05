import discord
from discord.ext import commands
import randomGenreGenerator
import randomPicker
import whoFirst as whoFirstFn
import bb3name
import guessLyricsGame
import data

env_vars = {}
with open('.env') as f:
    for line in f:
        if line.startswith('#') or not line.strip():
            continue
        key, value = line.strip().split('=', 1)
        env_vars[key] = value

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

intents = discord.Intents.default()
intents.message_content = True

#client = MyClient(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)

# client = discord.Client(intents=discord.Intents.default())

@bot.command()
async def newGenre(ctx: commands.Context):
    await ctx.reply(randomGenreGenerator.generator())
@bot.command()
async def picker(ctx: commands.Context):
    await ctx.reply(randomPicker.picker(ctx))
@bot.command()
async def whoFirst(ctx: commands.Context):
    await ctx.reply(whoFirstFn.picker(ctx))
@bot.command()
async def BB3Team(ctx: commands.Context):
    await ctx.reply(bb3name.bb3name())
@bot.command()
async def lyrics(ctx: commands.Context):
    await guessLyricsGame.guessLyricsGame(ctx)
@bot.command()
async def bothelp(ctx: commands.Context):
    await ctx.reply(data.helpText)


bot.run(env_vars['discord_access_token'])