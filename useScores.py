import json

with open('scores.json') as f:
    scores = json.load(f)

def getAllScores():
    return scores

def getScoreData(name):
    return scores[name]

def addScore(name, score, band, hints):
    # if its a new user, initialize their score
    if name not in scores:
        scores[name] = {
            'totalScore': 0, 
            'plays': 0,
            'wins': 0,
            'hints': 0,
            'bands': {}
        }
    if band not in scores[name]['bands']:
        scores[name]['bands'][band] = {
            'plays': 0,
            'wins': 0,
            'hints': 0
        }

    scores[name]['totalScore'] += score
    scores[name]['plays'] += 1
    scores[name]['bands'][band]['plays'] += 1

    if score > 0:
        scores[name]['bands'][band]['wins'] += 1
        scores[name]['wins'] += 1
        
    scores[name]['bands'][band]['hints'] += hints
    scores[name]['hints'] += hints
    
    with open('scores.json', 'w') as f:
        json.dump(scores, f)
