import sqlite3
from QuotePage import QuotePage
from Quote import Quote
import random
conn = sqlite3.connect('quotegame.db')
c = conn.cursor()

def fill_database_with_quotes(page_numbers):    
    website = QuotePage()
    
    quotes_list = website.get_quotes_multiple_pages(page_numbers)    
    print(f'{quotes_list}')
    print(f'{len(quotes_list)}')
    # save_quotes(quotes_list)

def create_database():

    
    sql_quotes_table="""
        CREATE TABLE IF NOT EXISTS quotes(
            quote varchar(250) NOT NULL,
            author VARCHAR(100) NOT NULL,
            born VARCHAR(100) NOT NULL,
            initials VARCHAR(10) NOT NULL
        )
    
    """
    with conn:
        c.execute(sql_quotes_table)
    
def save_quotes(quotes_list):
    
    sql = """
    INSERT INTO quotes VALUES(?,?,?,?)
    """
    with conn:
        c.execute("DELETE FROM quotes")
        for quote in quotes_list:
            c.execute(sql,(quote.quote, quote.author, quote.born_in, quote.initials))


def get_random_quote():
    with conn:
        sql = "Select count() from quotes"
        quote_count = c.execute(sql).fetchone()[0]
        quote_id = random.randint(1,quote_count)
        get_quote = "Select * from quotes where rowid=?"
        # print(get_quote)
        # print(quote_id)
        # print(type(quote_id))
        
        query_result = c.execute(get_quote,(quote_id))
        q = query_result.fetchone()
        quote = Quote(q[0],q[1],q[2])
        
    return quote

if __name__=="__main__":
    get_random_quote()