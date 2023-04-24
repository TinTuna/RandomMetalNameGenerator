import discord
import generateMap
import json

async def map():
    # await generateMap.generateMapImage()
    with open('images/heatmap.jpg', 'rb') as f:
        picture = discord.File(f)
    with open('bandCountriesData.json', 'r') as f:
        bandCountryData = json.load(f)
    # sort the data by the number of bands from each country
    bandCountryData = dict(sorted(bandCountryData.items(), key=lambda item: item[1], reverse=True))
    # get the top 10 countries
    top10 = list(bandCountryData.items())[:10]
    # convert the list of tuples to a string
    top10 = '\n'.join([str(elem) for elem in top10])
    # return piucture, top10
    return picture, top10