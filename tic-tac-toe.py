#W02 Prove: Developer - Solo Code Submission (Tic-Tac-Toe)
#Author: Alison Mazzarella-Woelzl

#setting up the tic-tac-toe board, dimensions are 3x3.

createBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

number_keypad = []

for number in createBoard: 
    number_keypad.append(number)

def printBoardgame(boardGame):
    print(boardGame['7'] + '|' + boardGame['8'] + '|' + boardGame['9'])
    print('-+-+-')
    print(boardGame['4'] + '|' + boardGame['5'] + '|' + boardGame['6'])
    print('-+-+-')
    print(boardGame['1'] + '|' + boardGame['2'] + '|' + boardGame['3'])

#establishing player one, and movement restrictions. 
def main():

    player1 = 'X'
    count = 0

    for i in range(10):
        printBoardgame(createBoard)
        print("It's your turn Player " + player1 + ". Please select a number on your keypad (1-9) to make your move.")

        move = input()

        if createBoard[move] == ' ':
            createBoard[move] = player1
            count += 1
        else: 
            print("You can't move there, please try again!")
            continue 

#establishing how to determine if there is a winner and who won. Parameters check after every 5 moves to see who the last player was to move, thereby determining possible winner.     
        if count >= 5: 

            if createBoard['7'] == createBoard['8'] == createBoard['9'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['4'] == createBoard['5'] == createBoard['6'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['1'] == createBoard['2'] == createBoard['3'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['7'] == createBoard['4'] == createBoard['1'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['8'] == createBoard['5'] == createBoard['2'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['9'] == createBoard['6'] == createBoard['3'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['7'] == createBoard['5'] == createBoard['3'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

            elif createBoard['9'] == createBoard['5'] == createBoard['1'] != ' ':
                printBoardgame(createBoard)
                print("Congrats! " + player1 + " has won the game!")
                break

#establishing rules in the event of a tie.
        if count == 9: 
            print("Sorry there are no more spaces to choose from. No one has won, therefore it is a tie!")

#establishing parameters to switch between player 1 & 2.
        if player1 == 'X':
            player1 = 'O'
        else:
            player1 = 'X'

#write program protocol if player wants to continue playing or quite.
    play_again = input("Do you want to play again? Type Yes or No.")
    while play_again == "Yes":
        if number in number_keypad:
            createBoard[number] = " " 
        main()
    else: 
        quit()

#call to main
if __name__ == "__main__":
    main()