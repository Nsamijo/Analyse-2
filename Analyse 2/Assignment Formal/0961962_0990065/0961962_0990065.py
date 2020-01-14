#written by:
# - 0961962 Nathan Samijo 
# - 0990065 Andrew Kasanredjo
class piggy:
    import random
    import msvcrt
    scores = []
    usernames = []
    maxPoints = 0

    def __init__(self):
        super().__init__()
        self.usernames = []
        self.scores = []
        self.maxPoints = 0

    def setup(self):
        '''setup the game'''
        print(50 * '*')
        print('\nWelcome to GAME OF PIG')
        print('\n' + 50 * '*')
        print('\nTo start the game, please setup the game: ')

        mode = input('\nPlease choose a game: "1": Beginners    "2": Advanced --- ')
        while mode not in ['1', '2']:
            mode = input('\nPlease choose a game: "1": Beginners    "2": Advanced --- ')

        if mode == '1':
            self.maxPoints = 50
        else:
            self.maxPoints = 100

        players = input('\nPlease enter the number of players (2-6): ')
        while players not in ['2', '3', '4' , '5' , '6']:
            players = input('\nPlease enter the number of players (2-6): ')
        
        for x in range(int(players)):
            name = input('\nEnter the name of player ' + str(x + 1) + ': ')
            while name == '' or name == ' ' or name in self.usernames:
                name = input('\nEnter the name of player ' + str(x + 1) + ': ')
            self.usernames.append(name)
            self.scores.append(0)

    def roll(self):
        '''roll the dice'''
        def printRolled(num):
            '''show what has been rolled'''
            print('\n' + 50 * '*')
            print(20 * '*' + ' Rolled ' + str(num) + ' ' + 20 * '*')
            print(50 * '*')
        temp = self.random.randint(1,6)
        printRolled(temp)
        return temp

    def message(self, rolled, points, turn):
        '''displays a message based on the amount rolled'''
        if rolled == 1:
            print('Oops! You lose ' + str(points) + ' but still keep your previous ' + str(self.scores[turn]))
        else:
            print('New Collected Score; ' + str(points) + ' + ' + str(rolled) + ' = ' + str(points + rolled))

    def currentScores(self):
        '''print the current scores'''
        print('\n' + 50 * '=')
        print('Total Safe Scores: ')
        for x in range(len(self.usernames)):
            print(self.usernames[x] + ' = ' + str(self.scores[x]))
    
    def check(self):
        '''checking if the maximum points have not been exceeded yet'''
        for x in self.scores:
            if x >= self.maxPoints:
                return True
        return False

    def turn(self, turn, first=False):
        '''shows who's turn it is'''
        name = self.usernames[turn]
        print(50 * '-')
        print('\nCurrent Player: ' + name)
        print('\nCurrent score at this turn: ' + str(self.scores[turn]))
        if first:
            print('\n' + name + ' your first dice will automatically be rolled')
            print('\nReady?')
        print('\nPress any key...')
        self.msvcrt.getch()

    def decision(self, turn):
        '''users have to decide what to do'''
        temp = input('\n' + self.usernames[turn] +  ', choose your next decision: "r": roll the dice     "p": pass the turn and save your score: ')
        while temp not in ['r', 'p']:
            print('Invalid Input')
            temp = input('You can choose: "r": to roll the dice or "p": to pass the turn and save your score: ')
        return temp

    def winner(self):
        '''prints the winner'''
        pos = None
        for x in self.scores:
            if x > self.maxPoints:
                pos = self.scores.index(x)

        print('\n' + self.usernames[pos] + ' won the game with a score of ' + str(self.scores[pos]) + ' *** ***')

    def safe(self, points, turn):
        '''saves the score of the current player if p is passed this functions is called'''
        self.scores[turn] += points
        
if __name__ == 'n__':
    turn = 0
    buffer = 0
    first = True
    decision = None
    pig = piggy()
    #setup the game
    pig.setup()
    #keep rolling till a player has exceeded the maximum points or reached it
    while not pig.check():

        #this loop keeps a player rolling
        while decision != 'p':
            pig.currentScores()
            pig.turn(turn, first)
            if first:
                first = False
            rolled = pig.roll()
            pig.message(rolled, buffer, turn)
            #break out of the loop if a 1 is rolled
            if rolled == 1:
                break
            buffer += rolled
            decision = pig.decision(turn)

        if decision == 'p' and rolled != 1:
            pig.safe(buffer, turn)

        #reset out variables for the next player
        turn += 1
        first = True
        decision = 'r'
        buffer = 0
        if turn > len(pig.usernames) - 1:
            turn = 0
    # winner winner chicken dinner
    pig.winner()