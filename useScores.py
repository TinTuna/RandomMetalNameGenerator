import json
import data
import random
import datetime
import math

with open('scores.json') as f:
    scores = json.load(f)

def getAllScores():
    return scores

def getScoreData(user_id):
    return scores[user_id]

def getScoreFormatted(user_id):
    # randomise random
    random.SystemRandom()
    # pick a random score message from data.affermativeWords
    scoreMessage = random.choice(data.affermativeWords)
    message = "Want stats? " + scoreMessage + ":\n\n"
    message += "Total Score: " + str(scores[user_id]['totalScore']) + "\n"
    message += "Total Plays: " + str(scores[user_id]['plays']) + "\n"
    message += "Wins: " + str(scores[user_id]['wins']) + "\n"
    message += "Losses: " + str(scores[user_id]['plays'] - scores[user_id]['wins']) + "\n"
    message += "Hints Used: " + str(scores[user_id]['hints']) + "\n\n"

    if scores[user_id]['bands'] == {}:
        return message + "Play some games to get more stats!"

    # count the number of times each band has been played
    multiple = False
    topBand = None
    topBandData = None
    for band in scores[user_id]['bands']:
        if topBand == None:
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['plays'] > topBandData['plays']:
            multiple = False
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['plays'] == topBandData['plays']:
            multiple = True
            
    # get the most frequent band
    if multiple:
        message += "Most Frequent Band Served: Multiple Bands\n"
    else:
        message += "Most Frequent Band Served: " + topBand + "\n"


    # count the number of times each band has been answered
    multiple = False
    topBand = None
    topBandData = None
    for band in scores[user_id]['bands']:
        if scores[user_id]['bands'][band]['wins'] == 0:
            continue
        if topBand == None:
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['wins'] > topBandData['wins']:
            multiple = False
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['wins'] == topBandData['wins']:
            multiple = True
            
    # get the most frequent band
    if multiple:
        message += "Most Frequent Band Won: Multiple Bands\n"
    elif topBand == None:
        message += "Most Frequent Band Won: None :cry:\n"
    else:
        message += "Most Frequent Band Won: " + topBand

    return message


def getScoreFormattedTable(user_id, user):
    if scores[user_id]['bands'] == {}:
        return user + ", play some games to get more stats!"

    # a long string os spaces
    spaces = '                                '
    # randomise random
    random.SystemRandom()
    # pick a random score message from data.affermativeWords
    scoreMessage = random.choice(data.affermativeWords)
    message = "Want stats? " + scoreMessage + ":\n\n"

    usernameLen = len(user)
    nameSpaces = spaces[:35 - usernameLen]

    totalScore = str(scores[user_id]['totalScore'])
    totalScoreLen = len(totalScore)
    totalScoreSpaces = spaces[:4 - totalScoreLen]

    if 'pointsToday' in scores[user_id]:
        pointsToday = str(scores[user_id]['pointsToday'])
        pointsTodayLen = len(pointsToday)
        pointsTodaySpaces = spaces[:4 - pointsTodayLen]
    else:
        pointsToday = '0'
        pointsTodayLen = len(pointsToday)
        pointsTodaySpaces = spaces[:4 - pointsTodayLen]

    totalPlays = str(scores[user_id]['plays'])
    totalPlaysLen = len(totalPlays)
    totalPlaysSpaces = spaces[:4 - totalPlaysLen]

    wins = str(scores[user_id]['wins'])
    winsLen = len(wins)
    winsSpaces = spaces[:4 - winsLen]

    losses = str(scores[user_id]['plays'] - scores[user_id]['wins'])
    lossesLen = len(losses)
    lossesSpaces = spaces[:4 - lossesLen]

    hints = str(scores[user_id]['hints'])
    hintsLen = len(hints)
    hintsSpaces = spaces[:4 - hintsLen]

    if 'streak' in scores[user_id]:
        streak = str(scores[user_id]['streak'])
        streakLen = len(streak)
        streakSpaces = spaces[:4 - streakLen]
    else:
        streak = '0'
        streakLen = len(streak)
        streakSpaces = spaces[:4 - streakLen]

    if 'streakMultiplier' in scores[user_id]:
        streakMultiplier = str(scores[user_id]['streakMultiplier'])
        streakMultiplierLen = len(streakMultiplier)
        streakMultiplierSpaces = spaces[:4 - streakMultiplierLen]
    else:
        streakMultiplier = '1'
        streakMultiplierLen = len(streakMultiplier)
        streakMultiplierSpaces = spaces[:4 - streakMultiplierLen]

    frequentBands = ''
    
    # count the number of times each band has been played
    multiple = False
    topBand = None
    topBandData = None
    for band in scores[user_id]['bands']:
        if topBand == None:
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['plays'] > topBandData['plays']:
            multiple = False
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['plays'] == topBandData['plays']:
            multiple = True
    
    # get the most frequent band
    if multiple:
        frequentBands += "Most Frequent Band Served: Multiple Bands\n"
    else:
        frequentBands += "Most Frequent Band Served: " + topBand + "\n"
    

    # count the number of times each band has been answered
    multiple = False
    topBand = None
    topBandData = None
    for band in scores[user_id]['bands']:
        if scores[user_id]['bands'][band]['wins'] == 0:
            continue
        if topBand == None:
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['wins'] > topBandData['wins']:
            multiple = False
            topBand = band
            topBandData = scores[user_id]['bands'][band]
        elif scores[user_id]['bands'][band]['wins'] == topBandData['wins']:
            multiple = True
    
    # get the most frequent band
    if multiple:
        frequentBands += "Most Frequent Band Won: Multiple Bands\n"
    elif topBand == None:
        frequentBands += "Most Frequent Band Won: None :cry:\n"
    else:
        frequentBands += "Most Frequent Band Won: " + topBand


    table =  '```\n'
    table += '+------------------------------------+\n'
    table += '| ' + user + nameSpaces + '|\n'
    table += '+-----------------------------+------+\n'
    table += '| Total Score                 | ' + totalScoreSpaces + str(totalScore) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Total Points Today          | ' + pointsTodaySpaces + str(pointsToday) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Total Plays                 | ' + totalPlaysSpaces + str(totalPlays) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Wins                        | ' + winsSpaces + str(wins) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Losses                      | ' + lossesSpaces + str(losses) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Streak                      | ' + streakSpaces + str(streak) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Streak Multiplier           | ' + streakMultiplierSpaces + str(streakMultiplier) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '| Hints Used                  | ' + hintsSpaces + str(hints) + ' |\n'
    table += '+-----------------------------+------+\n'
    table += '```\n\n'
    

    return message + table + frequentBands
    

def addScore(user_id, score, band, hints):
    today = str(datetime.datetime.today().date())
    # if its a new user, initialize their score
    if user_id not in scores:
        scores[user_id] = {
            'totalScore': 0, 
            'plays': 0,
            'wins': 0,
            'hints': 0,
            'lastPlayed': today,
            'pointsToday': 0,
            'streak': 0,
            'streakMultiplier': 1,
            'bands': {}
        }

    streakScore = math.floor(score * scores[user_id]['streakMultiplier'])
    
    # check if the user has played today
    if scores[user_id]['lastPlayed'] == today:
        # if they have, add the score to pointsToday
        scores[user_id]['pointsToday'] += streakScore
    else:
        # if they haven't, reset pointsToday
        scores[user_id]['pointsToday'] = score
    
    if band not in scores[user_id]['bands']:
        scores[user_id]['bands'][band] = {
            'plays': 0,
            'wins': 0,
            'hints': 0
        }

    scores[user_id]['totalScore'] += streakScore
    scores[user_id]['lastPlayed'] = today
    scores[user_id]['plays'] += 1
    scores[user_id]['bands'][band]['plays'] += 1

    if score > 0:
        scores[user_id]['bands'][band]['wins'] += 1
        scores[user_id]['wins'] += 1
        scores[user_id]['streak'] += 1
        scores[user_id]['streakMultiplier'] += 0.25
    else:
        scores[user_id]['streak'] = 0
        scores[user_id]['streakMultiplier'] = 1
        
    scores[user_id]['bands'][band]['hints'] += hints
    scores[user_id]['hints'] += hints
    
    with open('scores.json', 'w') as f:
        json.dump(scores, f)