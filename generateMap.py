import plotly.express as px
from kaleido.scopes.plotly import PlotlyScope
import csv
import os
import math
import getGoogleSheet
import json



# async def generateMapImage():
scope = PlotlyScope()
scope.chromium_args = tuple([arg for arg in scope.chromium_args if arg != "--disable-dev-shm-usage"])
scope.chromium_args

# if bandCountriesData.json does not exist
# get the data from the google sheet
# and write it to bandCountriesData.json
# if not os.path.exists("bandCountriesData.json"):
bandData = getGoogleSheet.main('2021')
bandData += getGoogleSheet.main('2022')
bandData += getGoogleSheet.main('2023')

# for each band, get the country and count it
bandCountryData = {}
for band in bandData:
    if band[0] == '':
        continue
    if band[2] == '':
        continue
    if band[2] not in bandCountryData:
        bandCountryData[band[2]] = 1
    else:
        bandCountryData[band[2]] += 1

# write the data to a csv file
with open('bandCountriesData.json', 'w') as f:
    json.dump(bandCountryData, f)
# else:
#     # open and read the data from the json file
#     with open('bandCountriesData.json', 'r') as f:
#         bandCountryData = json.load(f)

if not os.path.exists("images"):
    os.mkdir("images")

countriesDict = {"country": [], "iso_alpha": [], "iso_num": []}
with open('countriesData.csv', newline='') as csvfile:
    countries = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in countries:
        countriesDict["country"].append(row[0])
        countriesDict["iso_alpha"].append(row[2])
        countriesDict["iso_num"].append(row[3])

# gapminder = px.data.gapminder()

# f = open("demofile3.txt", "w")
# f.write(gapminder.to_string())
# f.close()

# # generate a list of random numbers between 0 and 3
list = []
listLog = []
for i in range(len(countriesDict["country"])):
    if countriesDict["iso_alpha"][i] in bandCountryData:
        list.append(bandCountryData[countriesDict["iso_alpha"][i]])
        listLog.append(math.log(bandCountryData[countriesDict["iso_alpha"][i]])+1)
    else:
        list.append(0)
        listLog.append(0)

countriesDict['counts'] = list
countriesDict['countsLog'] = listLog

fig = px.choropleth(countriesDict, locations="iso_alpha",
                    color="countsLog",
                    hover_name="country",
                    color_continuous_scale=px.colors.sequential.amp)
fig.update_coloraxes(showscale=False)

# fig.show()
fig.write_image("images/heatmap.jpg", width=4000, height=2000, scale=2, engine="kaleido", format="jpg")
