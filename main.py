#Simple rock, paper, scissors game for two players
#Author: @heyitsjanai


def welcome():
    """This function is just an instructions method"""
    print(
        'Welcome to Rock, Paper, Scissors!\n'
        'Grab a friend & get ready to play\n'
        'Type \'r\' for rock, \'s\' for scissors, or \'p\' for paper\n'
        'Type \'q\' to quit\n'
    )


def paperBeatsRock():
    """This function executes if paper vs. rock is played"""
    return 'Paper covers rock!'


def rockBeatsScissors():
    """This function executes if rock vs. scissors is played"""
    return 'Rock smashes scissors!'


def scissorsBeatsPaper():
    """This function executes if scissors vs. paper is played"""
    return 'Scissors cuts paper!'


def playerOneWins():
    """This function executes if player 1 wins"""
    return 'Player 1 wins!\n'


def playerTwoWins():
    """This function executes if player 2 wins"""
    return 'Player 2 wins!\n'


def who_wins(p1, p2):
    """This function determines what is played & who wins"""

    # First case: a tie - both players entered the same value
    if p1 == p2:
        print('It\'s a tie!\n')

    #Second case: player 1 plays ROCK
    elif p1 == 'r':
        #Calls appropriate functions when player 2 plays SCISSORS
        if p2 == 's':
            print(rockBeatsScissors())
            print(playerOneWins())
        #Calls appropriate functions when player 2 plays PAPER
        elif p2 == 'p':
            print(paperBeatsRock())
            print(playerTwoWins())

    #Third case: player 1 plays PAPER
    elif p1 == 'p':
        if p2 == 'r':
            #Calls appropriate functions when player 2 plays ROCK
            print(paperBeatsRock())
            print(playerOneWins())
        elif p2 == 's':
            #Calls appropriate functions when player 2 plays SCISSORS
            print(scissorsBeatsPaper())
            print(playerTwoWins())

    #Fourth case: player 1 plays SCISSORS
    elif p1 == 's':
        if p2 == 'r':
            #Calls appropriate functions when player 2 plays ROCK
            print(rockBeatsScissors())
            print(playerTwoWins())
        elif p2 == 'p':
            #Calls appropriate functions when player 2 plays PAPER
            print(scissorsBeatsPaper())
            print(playerOneWins())


#Infinite loop that executes over & over until one of the players enters 'q'
while True:
    #Calls the instructions function
    welcome()
    #asks for player 1 selection, then player 2 selection
    player1 = input('Player 1 goes first. Rock, paper, or scissors?\n')
    player2 = input('Player 2, you are next. Rock, paper, or scissors?\n')
    #First checks to see if either player wants to quit. If so, program terminates here
    if player1 == 'q' or player2 == 'q':
        print('Thanks for playing! Bye!')
        break
    #If BOTH players input is valid, the function to see who wins is called
    elif (player1 == 'r' or player1 == 's' or player1 == 'p') and (player2 == 'r' or player2 == 's' or player2 == 'p'):
        who_wins(player1, player2)
    #If either player enters an invalid entry, the game restarts
    else:
        print('Invalid entry. Try again!')