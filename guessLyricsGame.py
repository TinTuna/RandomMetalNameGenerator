import discord
from discord.ext import commands
import random
import lyricsDB

async def guessLyricsGame(ctx: commands.Context):
    """Asks the user a question to confirm something."""
    # Get the artist and song and lyrics
    artist, song, lyrics, wrongChoice1, wrongChoice2 = lyricsDB.getLyrics()

    view = Question(artist, song, wrongChoice1, wrongChoice2)

    await ctx.send(lyrics, view=view)
    # Wait for the View to stop listening for input...
    await view.wait()
    if view.value:
        print('Correct answer!')
    else:
        print('Wrong answer!')


class Question(discord.ui.View):
    def __init__(self, artist, song, wrongChoice1, wrongChoice2):
        super().__init__()
        self.value = None
        self.artist = artist
        self.song = song
        self.wrongChoice1 = wrongChoice1
        self.wrongChoice2 = wrongChoice2
        self.add_buttons()
    
    def add_buttons(self):
        # BUTTON ONE
        button_one = discord.ui.Button(label=self.artist, style=discord.ButtonStyle.green)
        async def op1(interaction: discord.Interaction):
            await interaction.response.send_message('Correct!')
            self.value = True
            self.stop()

        button_one.callback = op1

        # BUTTON TWO
        button_two = discord.ui.Button(label=self.wrongChoice1, style=discord.ButtonStyle.green)
        async def op2(interaction: discord.Interaction):
            await interaction.response.send_message('Wrong! The correct answer is ' + self.artist + ' with the song ' + self.song + '.')
            self.value = False
            self.stop()

        button_two.callback = op2

        # BUTTON THREE
        button_three = discord.ui.Button(label=self.wrongChoice2, style=discord.ButtonStyle.green)
        async def op3(interaction: discord.Interaction):
            await interaction.response.send_message('Wrong! The correct answer is ' + self.artist + ' with the song ' + self.song + '.')
            self.value = False
            self.stop()

        button_three.callback = op3

        # add buttons in random order
        buttonList = [button_one, button_two, button_three]
        random.SystemRandom()
        random.shuffle(buttonList)
        self.add_item(buttonList[0])
        self.add_item(buttonList[1])
        self.add_item(buttonList[2])