import discord
from discord.ext import commands
import random
import lyricsDB
import useScores

async def guessLyricsGame(ctx: commands.Context):
    """Asks the user a question to confirm something."""
    # Get the artist and song and lyrics
    artistData, artist, album, song, lyrics, wrongChoice1, wrongChoice2 = await lyricsDB.getLyrics()

    view = Question(ctx, artistData, artist, album, song, wrongChoice1, wrongChoice2)

    await ctx.send('**Ok, tell me what band this is?**\n\n>>> '+lyrics, view=view)
    # Wait for the View to stop listening for input...
    await view.wait()


class Question(discord.ui.View):
    def __init__(self, ctx, artistData, artist, album, song, wrongChoice1, wrongChoice2):
        super().__init__()
        self.ctx = ctx
        self.artistData = artistData
        self.artist = artist
        self.album = album
        self.song = song
        avgHint = 'The average score for the album was ' + str(artistData['albums'][album]['avgScore'])
        author = str(ctx.message.author)
        if author == 'TinTuna#2453' or author == 'Tinngles#8236' or author == 'Izual#1552':
            if artistData['albums'][album][author] != '':
                avgHint += '\n' + ctx.message.author.mention + ' you scored it ' + str(artistData['albums'][album][author])
            else:
                avgHint += '\n' + ctx.message.author.mention + ' you have not scored this album yet.'
        self.hints = ['The album title ' + album, 
                      'The song title is ' + song, 
                      'The album was from ' + artistData['albums'][album]['date'], 
                      avgHint
                      ]
        self.wrongChoice1 = wrongChoice1
        self.wrongChoice2 = wrongChoice2
        self.ans = 'It was ' + artist + ' with the song ' + song + ' from the album ' + album + ' from ' + artistData['albums'][album]['date'] + '.'
        self.add_buttons()
    
    def add_buttons(self):
        # BUTTON ONE
        button_one = discord.ui.Button(label=self.artist, style=discord.ButtonStyle.primary)
        async def op1(interaction: discord.Interaction):
            # if the autor is not the original author, return
            if self.checkUser(interaction, self.ctx.author) == False:
                return
            await interaction.response.send_message('**'+self.artist+'**  '+'Correct! ' + self.ans)
            self.closeOut(interaction)
        button_one.callback = op1

        # BUTTON TWO
        button_two = discord.ui.Button(label=self.wrongChoice1, style=discord.ButtonStyle.primary)
        async def op2(interaction: discord.Interaction):
            # if the autor is not the original author, return
            if self.checkUser(interaction, self.ctx.author) == False:
                return
            await interaction.response.send_message('**'+self.wrongChoice1+'**  '+'Wrong! ' + self.ans)
            self.closeOut(interaction)
        button_two.callback = op2

        # BUTTON THREE
        button_three = discord.ui.Button(label=self.wrongChoice2, style=discord.ButtonStyle.primary)
        async def op3(interaction: discord.Interaction):
            # if the autor is not the original author, return
            if self.checkUser(interaction, self.ctx.author) == False:
                return
            await interaction.response.send_message('**'+self.wrongChoice2+'**  '+'Wrong! ' + self.ans)
            self.closeOut(interaction)
            
        button_three.callback = op3

        # add buttons in random order
        buttonList = [button_one, button_two, button_three]
        random.SystemRandom()
        random.shuffle(buttonList)
        self.add_item(buttonList[0])
        self.add_item(buttonList[1])
        self.add_item(buttonList[2])

        button_hint = discord.ui.Button(label='Give me a hint', custom_id="button-hint", style=discord.ButtonStyle.green)
        async def hint(interaction: discord.Interaction):
            # if the autor is not the original author, return
            if self.checkUser(interaction, self.ctx.author) == False:
                return
            random.SystemRandom()
            random.shuffle(self.hints)
            if len(self.hints) > 1:
                await interaction.response.send_message(self.hints.pop())
            elif len(self.hints) == 1:
                self.remove_item(button_hint)
                await interaction.response.edit_message(view=self)
                await interaction.followup.send(self.hints.pop())
            else:
                await interaction.response.send_message('No more hints left!')
        
        button_hint.callback = hint
        self.add_item(button_hint)

        self.button_one = button_one
        self.button_two = button_two
        self.button_three = button_three
        self.button_hint = button_hint

    async def closeOut(self, interaction):
        hintsUsed = 4 - len(self.hints)
        score = 5 - hintsUsed
        self.remove_item(self.button_hint)
        self.remove_item(self.button_two)
        self.remove_item(self.button_three)
        self.button_one.disabled = True
        await interaction.followup.edit_message(view=self, message_id=interaction.message.id)
        useScores.addScore(self.ctx.message.author, score, self.artist, hintsUsed)
        self.stop()
        
    async def checkUser(self, interaction, user):
        if interaction.user != user:
            await interaction.response.send_message('Dont be stealing other peoples games, '+ interaction.user.mention, ephemeral=True)
            return False
        return True

