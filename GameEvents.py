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
goal = 0
foul = 1
corner = 2
offside = 3
yellow_card = 4
red_card = 5
penalty = 6
fastbreak = 7
attempt_1 = 8
attempt_2 = 9
attempt_3 = 10
attempt_4 = 11
attempt_5 = 12
attempt_6 = 13
attempt_7 = 14
attempt_8 = 15
attempt_9 = 16
attempt_10 = 17
attempt_11 = 18
attempt_12 = 19
attempt_13 = 20
attempt_14 = 21
attempt_15 = 22
attempt_16 = 23
attempt_17 = 24
attempt_18 = 25
attempt_19 = 26
country = 27

    
class Event:    
    event = []
    
    def __init__(self, eventList):
        self.event = eventList

class Game:
    game = []
    home = 0
    away = 0
    
    def __init__(self):
        self.game = ['0'] * 28
        
    def setCountry(self, thiscountry):
        self.game[country] = thiscountry
          
    
if (len(sys.argv) != 3 and len(sys.argv) != 4) :
    print('Usage: GameEvents.py <InputCSVfilePath> <InputCSVfilePath> (<OutputCSVFile>)\n')
    sys.exit()

if (len(sys.argv) == 3):
    outfile = 'gameEvents.csv'
elif (len(sys.argv) == 4):
    outfile = sys.argv[3]
    
# Game Events 
events = []

# Extract events from CSV file
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

# Countries
countries = []
         
# Extract countries from CSV file
with open(sys.argv[2], encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in list(csv_reader):
        if line_count == 0:
            line_count += 1
        else:
            game_id = row[0]
            countr = row[6]
            countries.append([game_id, countr])
            
            
# Games
games = []
game = Game()

# Sum Game Events
currentEvent = events[0].event[id_odsp]
currentEventNo = 0
for event in events:
    if (event.event[id_odsp] != currentEvent):
        if (countries[currentEventNo][0] != currentEvent):
            print(currentEvent)
            print(countries[currentEventNo][0])
            err = 'Error getting country (line ' + str(currentEventNo + 1) + ')'
            print(err)
            currentEventNo = currentEventNo + 1
            c = "NA"
        else: c = countries[currentEventNo][1]
        g = copy.deepcopy(game)         
        g.setCountry(c)
        games.append(g.game)
        currentEvent = event.event[id_odsp]
        currentEventNo = currentEventNo + 1
        game = Game()
    
    # Goal
    if (event.event[is_goal] == '1'):
        game.game[goal] = str(int(game.game[goal]) + 1)

    # Corner
    if (event.event[event_type] == '2'):  
        game.game[corner] = str(int(game.game[corner]) + 1)
    
    # Foul
    elif (event.event[event_type] == '3'): 
        game.game[foul] = str(int(game.game[foul]) + 1)
    
    # Yellow Card
    elif (event.event[event_type] == '4'): 
        game.game[yellow_card] = str(int(game.game[yellow_card]) + 1)
    
    # Second Yellow Card
    elif (event.event[event_type] == '5'): 
        game.game[yellow_card] = str(int(game.game[yellow_card]) + 1)
        game.game[red_card] = str(int(game.game[red_card]) + 1)
    
    # Red Card
    elif (event.event[event_type] == '6'): 
        game.game[red_card] = str(int(game.game[red_card]) + 1)
    
    # Offside
    elif (event.event[event_type] == '9'): 
        game.game[offside] = str(int(game.game[offside]) + 1)
    
    # Penalty
    elif (event.event[event_type] == '11'): 
        game.game[penalty] = str(int(game.game[penalty]) + 1)
    
    # Attempt
    elif (event.event[event_type] == '1'): 
        if (event.event[location] == '1'):
            game.game[attempt_1] = str(int(game.game[attempt_1]) + 1)
        elif (event.event[location] == '2'):
            game.game[attempt_2] = str(int(game.game[attempt_2]) + 1)
        elif (event.event[location] == '3'):
            game.game[attempt_3] = str(int(game.game[attempt_3]) + 1)
        elif (event.event[location] == '4'):
            game.game[attempt_4] = str(int(game.game[attempt_4]) + 1)
        elif (event.event[location] == '5'):
            game.game[attempt_5] = str(int(game.game[attempt_5]) + 1)
        elif (event.event[location] == '6'):
            game.game[attempt_6] = str(int(game.game[attempt_6]) + 1)
        elif (event.event[location] == '7'):
            game.game[attempt_7] = str(int(game.game[attempt_7]) + 1)
        elif (event.event[location] == '8'):
            game.game[attempt_8] = str(int(game.game[attempt_8]) + 1)
        elif (event.event[location] == '9'):
            game.game[attempt_9] = str(int(game.game[attempt_9]) + 1)
        elif (event.event[location] == '10'):
            game.game[attempt_10] = str(int(game.game[attempt_10]) + 1)
        elif (event.event[location] == '11'):
            game.game[attempt_11] = str(int(game.game[attempt_11]) + 1)
        elif (event.event[location] == '12'):
            game.game[attempt_12] = str(int(game.game[attempt_12]) + 1)
        elif (event.event[location] == '13'):
            game.game[attempt_13] = str(int(game.game[attempt_13]) + 1)
        elif (event.event[location] == '14'):
            game.game[attempt_14] = str(int(game.game[attempt_14]) + 1)
        elif (event.event[location] == '15'):
            game.game[attempt_15] = str(int(game.game[attempt_15]) + 1)
        elif (event.event[location] == '16'):
            game.game[attempt_16] = str(int(game.game[attempt_16]) + 1)
        elif (event.event[location] == '17'):
            game.game[attempt_17] = str(int(game.game[attempt_17]) + 1)
        elif (event.event[location] == '18'):
            game.game[attempt_18] = str(int(game.game[attempt_18]) + 1)
        elif (event.event[location] == '19'):
            game.game[attempt_19] = str(int(game.game[attempt_19]) + 1)
    
# Labels
labels = ['goal','foul','corner','offside','yellow_card','red_card','penalty','fastbreak','attempt_1','attempt_2','attempt_3','attempt_4','attempt_5','attempt_6','attempt_7','attempt_8','attempt_9','attempt_10','attempt_11','attempt_12','attempt_13','attempt_14','attempt_15','attempt_16','attempt_17','attempt_18','attempt_19','country']

# Export to CSV file
with open(outfile, mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    csv_writer.writerow(labels)
    
    for game in games:
        csv_writer.writerow(game)