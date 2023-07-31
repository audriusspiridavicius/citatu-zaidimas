import random

from Quote import Quote


class Game:
    def __init__(self, quote):
        print(quote)
        print(type[quote])
        self.quote = quote
        self.data_input_rovider = ""
        
    # @property
    # def quote(self):
    #     return self.quotes


    def play_game(self):
        quote_data = self.quote

        attempt = 1
        hint = ""
        while True:
            # maybe put attempt to settings class/object and then add to game different settings or something like that
            if attempt == 2:
                hint = quote_data.initials
            if attempt == 3:
                hint = quote_data.born_in
            guess = self.guess(hint) # guess provider or something like that??? not sure how to name it
            if guess == quote_data.author:
                print("winner")
                break
            elif guess != quote_data.author and attempt == 3:
                print("lost")
                print(f"the quote: {quote_data.quote}")
                print(f"by: {quote_data.author}")
                break
            attempt += 1

    def guess(self, hint):
        print(hint)
        guess_text = input("Please enter your guess: ")
        return guess_text

