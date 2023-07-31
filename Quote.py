class Quote:
    def __init__(self, quote, author, born_in=""):
        self.quote = quote
        self.author = author
        self.born_in = born_in
        self.initials = f"{self.author[0]}.{self.author.split()[1][0]}"
