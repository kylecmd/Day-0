import random
import time
playerOneScore = 0
playerTwoScore = 0

for i in range(5):
    print("It is Player One's Turn \nType 'roll' to roll your dice , type 'quit' to end your turn or 'exit' to end the game.")

    plrOneInput = input(">>>")
    if plrOneInput == "roll":
        rolledOne = random.randint(1,6)
        print("Player 1 rolled", rolledOne)
        print("It is now player Two's turn \nType 'roll' to roll your dice , type 'quit' to end your turn or 'exit' to end the game.")
        plrTwoInput = input(">>>")
        if plrTwoInput == "roll":
            rolledTwo = random.randint(1,6)
            print("Player 2 rolled", rolledTwo)
            if rolledOne > rolledTwo:
                playerOneScore += 1
                print("Player 1 wins a point!","\nPlayer 1 :", playerOneScore, "\nplayer 2:", playerTwoScore)
            elif rolledOne == rolledTwo:
                print("Womp Womp , it's a tie!")
            else:
                playerTwoScore += 1
                print("Player 2 wins a point!","\nPlayer 1 :", playerOneScore, "\nplayer 2:", playerTwoScore)
        elif plrTwoInput == "quit":
            playerOneScore += 1
            print("Player 2 forfeited this round! Player 1 wins a point!", "\nPlayer 1 :", playerOneScore, "\nplayer 2:", playerTwoScore )
        else:
            plrTwoInput == "exit"
            print("Welp Game Ended!   \n Thanks for Playing!")
            break
        time.sleep(2)

        """trying player 2 and the quits and exit under player 1's elif"""
    elif plrOneInput == "quit":
        playerTwoScore += 1
        print("Player 1 forfeited this round! Player 2 wins a point!","\nPlayer 1 :", playerOneScore, "\nplayer 2:", playerTwoScore)

    else:
        plrOneInput == "exit"
        print("Welp Game Ended!   \n Thanks for Playing!")
        break
    time.sleep(2)