# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:29:38 2020

@author: tiago
"""

import sys
import csv
import copy

# Event indexes
id_odsp = 0
event_type = 5
side = 7
is_goal = 16
location = 17
fast_break = 21

# Game indexes
foul = 0
corner = 1
offside = 2
yellow_card = 3
red_card = 4
penalty = 5
fastbreak = 6
attempt_1 = 7
attempt_2 = 8
attempt_3 = 9
attempt_4 = 10
attempt_5 = 11
attempt_6 = 12
attempt_7 = 13
attempt_8 = 14
attempt_9 = 15
attempt_10 = 16
attempt_11 = 17
attempt_12 = 18
attempt_13 = 19
attempt_14 = 20
attempt_15 = 21
attempt_16 = 22
attempt_17 = 23
attempt_18 = 24
attempt_19 = 25
winner = 52
# offsets
home = 0
away = 26
    
class Event:    
    event = []
    
    def __init__(self, eventList):
        self.event = eventList

class Game:
    game = []
    home = 0
    away = 0
    
    def __init__(self):
        self.game = [0] * 53
        
    def setWinner(self):
        if self.home > self.away:
            self.game[winner] = 1
        elif self.home < self.away:
            self.game[winner] = 2
        else:
            self.game[winner] = 0
          
    
if (len(sys.argv) != 2 and len(sys.argv) != 3) :
    print('Usage: HomeAwayGameEvents.py <InputCSVfilePath> (<OutputCSVFile>)\n')
    sys.exit()

if (len(sys.argv) == 3):
    outfile = 'gameEvents[HomeAway].csv'
elif (len(sys.argv) == 4):
    outfile = sys.argv[2]
    
# Game Events 
events = []

# Extract from CSV file
with open(sys.argv[1], encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in list(csv_reader):
        if line_count == 0:
            line_count += 1
        else:
            event = Event(row)
            events.append(event)
            line_count += 1
            

# Games
games = []
game = Game()

# Sum Game Events
currentEvent = events[0].event[id_odsp]
for event in events:
    if (event.event[id_odsp] != currentEvent):
        currentEvent = event.event[id_odsp]
        g = copy.deepcopy(game)
        g.setWinner()
        games.append(g.game)
        game = Game()
    
    if (event.event[side] == '1'):
        offset = home
        if (event.event[is_goal] == '1'):
            game.home = game.home + 1
    else:
        offset = away
        if (event.event[is_goal] == '1'):
            game.away = game.away + 1
    
    #Fastbreak
    if (event.event[fast_break] == '1'):
        game.game[fastbreak + offset] = game.game[fastbreak + offset] + 1

    # Corner
    if (event.event[event_type] == '2'):  
        game.game[corner + offset] = game.game[corner + offset] + 1
    
    # Foul
    elif (event.event[event_type] == '3'): 
        game.game[foul + offset] = game.game[foul + offset] + 1
    
    # Yellow Card
    elif (event.event[event_type] == '4'): 
        game.game[yellow_card + offset] = game.game[yellow_card + offset] + 1
    
    # Second Yellow Card
    elif (event.event[event_type] == '5'): 
        game.game[yellow_card + offset] = game.game[yellow_card + offset] + 1
        game.game[red_card + offset] = game.game[red_card + offset] + 1
    
    # Red Card
    elif (event.event[event_type] == '6'): 
        game.game[red_card + offset] = game.game[red_card + offset] + 1
    
    # Offside
    elif (event.event[event_type] == '9'): 
        game.game[offside + offset] = game.game[offside + offset] + 1
    
    # Penalty
    elif (event.event[event_type] == '11'): 
        game.game[penalty + offset] = game.game[penalty + offset] + 1
    
    # Attempt
    elif (event.event[event_type] == '1'): 
        if (event.event[location] == '1'):
            game.game[attempt_1 + offset] = game.game[attempt_1 + offset] + 1
        elif (event.event[location] == '2'):
            game.game[attempt_2 + offset] = game.game[attempt_2 + offset] + 1
        elif (event.event[location] == '3'):
            game.game[attempt_3 + offset] = game.game[attempt_3 + offset] + 1
        elif (event.event[location] == '4'):
            game.game[attempt_4 + offset] = game.game[attempt_4 + offset] + 1
        elif (event.event[location] == '5'):
            game.game[attempt_5 + offset] = game.game[attempt_5 + offset] + 1
        elif (event.event[location] == '6'):
            game.game[attempt_6 + offset] = game.game[attempt_6 + offset] + 1
        elif (event.event[location] == '7'):
            game.game[attempt_7 + offset] = game.game[attempt_7 + offset] + 1
        elif (event.event[location] == '8'):
            game.game[attempt_8 + offset] = game.game[attempt_8 + offset] + 1
        elif (event.event[location] == '9'):
            game.game[attempt_9 + offset] = game.game[attempt_9 + offset] + 1
        elif (event.event[location] == '10'):
            game.game[attempt_10 + offset] = game.game[attempt_10 + offset] + 1
        elif (event.event[location] == '11'):
            game.game[attempt_11 + offset] = game.game[attempt_11 + offset] + 1
        elif (event.event[location] == '12'):
            game.game[attempt_12 + offset] = game.game[attempt_12 + offset] + 1
        elif (event.event[location] == '13'):
            game.game[attempt_13 + offset] = game.game[attempt_13 + offset] + 1
        elif (event.event[location] == '14'):
            game.game[attempt_14 + offset] = game.game[attempt_14 + offset] + 1
        elif (event.event[location] == '15'):
            game.game[attempt_15 + offset] = game.game[attempt_15 + offset] + 1
        elif (event.event[location] == '16'):
            game.game[attempt_16 + offset] = game.game[attempt_16 + offset] + 1
        elif (event.event[location] == '17'):
            game.game[attempt_17 + offset] = game.game[attempt_17 + offset] + 1
        elif (event.event[location] == '18'):
            game.game[attempt_18 + offset] = game.game[attempt_18 + offset] + 1
        elif (event.event[location] == '19'):
            game.game[attempt_19 + offset] = game.game[attempt_19 + offset] + 1
    
# Labels
labels = ['home_foul','home_corner','home_offside','home_yellow_card','home_red_card','home_penalty','home_fastbreak','home_attempt_1','home_attempt_2','home_attempt_3','home_attempt_4','home_attempt_5','home_attempt_6','home_attempt_7','home_attempt_8','home_attempt_9','home_attempt_10','home_attempt_11','home_attempt_12','home_attempt_13','home_attempt_14','home_attempt_15','home_attempt_16','home_attempt_17','home_attempt_18','home_attempt_19','away_foul','away_corner','away_offside','away_yellow_card','away_red_card','away_penalty','away_fastbreak','away_attempt_1','away_attempt_2','away_attempt_3','away_attempt_4','away_attempt_5','away_attempt_6','away_attempt_7','away_attempt_8','away_attempt_9','away_attempt_10','away_attempt_11','away_attempt_12','away_attempt_13','away_attempt_14','away_attempt_15','away_attempt_16','away_attempt_17','away_attempt_18','away_attempt_19','winner']

# Export to CSV file
with open(outfile, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(labels)
    
    for game in games:
        csv_writer.writerow(game)