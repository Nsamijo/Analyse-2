import random
import matplotlib.pyplot as plot

#wins from strategies
strategies = [0, 0, 0]

#points from the strategies
points = [0, 0, 0]

#turn || which strategy should happen
turn = 0

#rolled amount
rolled = 0

#wins ending
MAX_WINS = 20

#max points limit
MAX_POINTS = 50

#dice rolling
def dice():
    #roll the dice and return this
    return random.randint(1, 6)

#strategies from the players
def strateGies(player):
    global turn, rolled, points
    #all strategies go here
    if player == 0:
        #player 1 || go till 12
        if rolled >= 12:
            #add the points to the total
            points[0] += rolled
            #reset the rolled
            rolled = 0
            #next player
            turn += 1
    elif player == 1:
        #player 2 || go till 33
        if rolled >= 33:
            #add the points to the total
            points[1] += rolled
            #reset the points
            rolled = 0
            #next player
            turn += 1
    elif player == 2:
        #player 3 || your strategy
        turn += 1
        pass

    #limit the turn to the amount of players
    if turn > 2:
        #reset the turn to the first player
        turn = 0

#pig game
def piggy():
    global rolled, turn
    #roll the dice
    temp = dice()

    #end the players turn and lose all the points
    if temp == 1:
        #player loses all points
        rolled = 0
        #next player
        turn += 1
    #if not a 1 (one) is rolled go to the strategy
    elif temp > 1:
        #add to the rolled, so this does not get lost
        rolled += temp
        #go to the players strategy
        strateGies(turn)

#here the program will do the computing
def research():
    #get the max variables
    global MAX_POINTS, MAX_WINS
    #get the points, rolled, turn and strategies
    global strategies, rolled, points

    #keep running the greedy pig till the max wins are achieved
    while sum(strategies) != MAX_WINS:
        
        #while the biggest is smaller then the maximum points to win 1 game, keep the game running
        while not max(points) > MAX_POINTS:
            #run the pig game once
            piggy()

        #dubbel check if is valid || is maybe not needed but you can never be sure
        if max(points) > MAX_POINTS:
            #get the winning strategy
            player = points.index( max(points) )
            #increment the winning strategy with 1
            strategies[player] += 1

            #reset the value to rerun the pig and stop bad data
            points = [0, 0, 0]

#bar chart creation
def draw():
    #get the points and the max wins
    global strategies, MAX_WINS

    #add all data to the chart individually otherwise it will be recognised as one chart
    for x in range(3):
        plot.bar(x, strategies[x], label='Strategy ' + str(x + 1))
    
    #set the labels
    plot.xlabel('Strategy')
    plot.ylabel('Winning Probability')

    #set the X-axis
    plot.xticks([0, 1, 2, 3], ['1', '2', '3'])

    #set the titel
    plot.title('Pig Game Winning Probabilities')

    #put the small window with the labels
    plot.legend()

    #show the graph
    plot.show()

#do the research
research()
#show the research
draw()
print(strategies)