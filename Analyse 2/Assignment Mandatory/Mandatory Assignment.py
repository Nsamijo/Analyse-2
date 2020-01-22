import random
import matplotlib.pyplot as plot
import numpy as np

#amount of players
players = ['Strategy ' + str(x) for x in range(1, 4)]
#amount of turns
turns = [0, 0 ,0]
#amount of rolls
rolls = [0, 0, 0]
#points from all the players
points = [0, 0, 0]
#player turn
turn = 0
#for how many we have rolled
rolled = 0
#turns for strategy 3 and checkpoint setting
checkPoint = 0
setPoint = True

#total wins
wins = [0, 0, 0]
win = 0

def nextPlayer():
    '''go to the next player'''
    global turn, setPoint, rolled
    #increment the turn
    turn += 1
    #if we surpassed the number of strategies turn gets reset to 0 || use of 2 because of list index
    if turn > 2:
        #reset turn
        turn = 0
    #reset rolled
    rolled = 0
    #reset the setpoint
    setPoint = True

def playerStrategy():
    '''here we have the strategies of the players'''
    global turn, turns, rolls, rolled, points
    #check which limit should we abide to
    if rolled >= [12, 33][turn]:
        #add what is rolled to the totel of rolls and turns
        rolls[turn] += rolled
        points[turn] += rolled
        #reset whar is rolled so that the next player does not inherit it
        rolled = 0
        #next player
        nextPlayer()

def strategy3():
    '''strategy 3 || OP'''
    global checkPoint, turns, setPoint
    global rolls, rolled, points
    #save the point before out turn once
    if setPoint:
        #set a checkpoint
        checkPoint = turns[2]
        #set it False so we only do this once
        setPoint = False

    #check if we have rolled a number of times
    if turns[2] - checkPoint == 6:
        #add what is rolled to the total points and rolls
        rolls[2] += rolled
        points[2] += rolled
        #next player
        nextPlayer()

def greedyPig():
    '''this is the function for greedy pig'''
    global rolled, turns, turn, rolls

    def roll():
        '''return a number'''
        return random.randint(1, 6)

    #roll and check what we have and increment turns
    temp = roll()
    #increment turns to know how many times we rolled
    turns[turn] += 1
    if temp == 1:
        #reset the rolled
        rolled = 0
        #next player
        nextPlayer()
    else:
        #increment the rolled variable so the total rolled is saved
        rolled += temp

        #check if strategy 1 or 2 are to go
        if turn < 2:
            #infidels strategies 
            playerStrategy()
        else:
            #time for our strategy to shine
            strategy3()

def check():
    '''check for the ending points'''
    global points, wins, win
    #check if we have a winner
    for x in points:
        #check if a strategy has surpassed the limit of points
        if x >= 50:
            #increment the points for the winning strategy
            wins[points.index(x)] += 1
            #return False to break out of the while loop
            return False
    return True

#run till we reach maximum wins
while sum(wins) != 100:
    #reset the points
    points = [0, 0, 0]
    
    #run greedy pig till we have a winner
    while check():
        #run greedy pig
        greedyPig()

#calculate the percentage
percent = []
for x in wins:
    percent.append(int(x/100 * 100))

#plot the data || set evenly spaced data for the X-axis
xpos = np.arange(len(players))

#set the max for the Y-axis
plot.axis(ymax=100)

#plot the bars individually
for x in range(3):
    plot.bar(x, percent[x], label=players[x] +' (' +str(percent[x]) + '%)', color=['red', 'grey', 'blue'][x])

#set the X-axis
plot.xticks(yxos, range(1, 4))

#set labels, title and then show the plot
plot.xlabel('Strategies')
plot.ylabel('Win Percentage')
plot.title('Probability of winning Pig Game')

#show the label for the bars
plot.legend()

#show the plot
plot.show()