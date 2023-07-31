from functions import create_database,fill_database_with_quotes, get_random_quote
from game import Game

while True:
    print("1 - update uotes list")
    print("2 - play game")
    print("0 - exit program")
    
    choice = input("Please enter your choice ")
    
    if choice=="0":
        exit()
    elif choice=="1":
        create_database()
        fill_database_with_quotes([1,2,3,4,5])
    elif choice=="2":

        random_quote = get_random_quote()
        game = Game(random_quote)
        game.play_game()