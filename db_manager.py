import sqlite3

def init_db(): 
    # creator or connect to handle db 
    conn = sqlite3.connect('handle.db')
    #create cursor
    c = conn.cursor()
    # save the chnages to the db 
    # create a table using c 
    c.execute("""CREATE TABLE handles (
        handle text, 
        tested text
        )
    """)
    conn.commit()
    # close the connection to the db 
    conn.close()
    