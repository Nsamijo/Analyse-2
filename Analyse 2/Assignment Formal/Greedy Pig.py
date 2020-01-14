#greedy pig
import msvcrt
import random 

players = {}
names = []
turn = 0
maxPoints = 0

def startGame():
    print('**************************************************************************************')
    print('Welcome to GAME OF PIG')
    print('**************************************************************************************')
    print('To start the game, please set up the game: ')

def gameSetup():
    global players, names, maxPoints

    def gameSort():
        print('\n')
        return input("Please choose a game: '1': Beginners     '2': Advanced --- ")

    def playersAmount():
        return input('\nPlease enter the number of players (2-6): ')
    
    def username(num):
        global players
        name = input('\nEnter the name of player ' + str(num) + ': ')
        while name == '' and name == '' and not name in players.keys():
            name = input('\nEnter the name of player ' + str(num) + ': ')
        return name

    def updateUsernames():
        global players, names
        for x in range(int(playersCount)):
            players.update({ username(x + 1): 0})
        
        for x in players.keys():
            names.append(x)

    mode = gameSort()
    while mode not in ['1','2']:
        mode = gameSort()
    if mode == '1':
        maxPoints = 50
    else:
        maxPoints = 100
    
    playersCount = playersAmount()
    while playersCount not in ['2', '3', '4', '5', '6']:
        playersCount = playersAmount()
    
    updateUsernames()

def game():
    global names, turn, players
    endTurn = False
    first = True
    def printScores():
        print()
        print('======================================================================================')
        print('Total Safe Scores')
        print()

        for name in players:
            print(name + ' = ' + str(players[name]))

    def randomPoints():
        return random.randint(1,6)

    def safe(pos,points):
        global players, names
        players[names[pos]] += points

    def currentPlayer(pos, first):
        print('-' * 50)
        print('Current Player: ' + names[pos])
        print('Current score at this turn:   ' + str(players[names[pos]]))
        print()
        if first:
            print(names[pos] + ' your first dice at this turn will be automatically rolled!')
        print('\n' + 'Ready?')
        print('press a key to continue...\n')
        msvcrt.getch()
    
    def rolled(points, temp):
        print(50 * '*')
        print(20 * '*' + ' Rolled ' + str(points) + ' ' + 20 * '*')
        print(50 * '*')
        print('new collected score = ' + str(temp) + ' + ' + str(points) + ' = '+ str(temp + points))

    def rolledOne(pos, temp):
        print(50 * '*')
        print(20 * '*' + ' Rolled 1 ' + 20 * '*')
        print(30 * '*' + 'Oops! You lose ' + str(temp) + ' but still keep your previous ' + str(players[names[pos]]))

    def check():
        temp = None
        for x in players.values():
            temp = maxPoints > x
            if not temp:
                return False
        return True

    def decision():
        temp = input(names[turn] + ', choose your next decision: "r": roll the dice     "p": pass the turn and save your score: ')
        while temp not in ['r', 'p']:
            print('Invalid input')
            temp = input('You can choose: "r": to roll the dice or "p": to pass the turn and save your score: ')
        return temp

    roll = 0
    temp = 0
    while check():
        while not endTurn:
            printScores()
            currentPlayer(turn, first)
            roll = randomPoints()
            if first:
                first = False
            if roll == 1:
                rolledOne(turn, temp)
                break
            rolled(roll, temp)
            temp += roll
            chosen = decision()
            if chosen == 'p':
                safe(turn, temp)
                endTurn = True

        if turn < len(names) - 1:
            turn += 1
        else:
            turn = 0
        
        endTurn = False
        first = True
        temp = 0
    
    printScores()
    temp = None
    scores = []
    for x in players.values():
        scores.append(x)
    for x in scores:
        if maxPoints < x:
            temp = scores.index(x)
    print('     ' + names[temp] + ' won the game with a score of ' + str(players[names[temp]]) + ' *** ***')


if __name__ == '__main__':
    startGame()
    gameSetup()
    game()