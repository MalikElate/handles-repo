import sqlite3

def init_db(): 
    conn = sqlite3.connect('handle.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS handles (
        handle text, 
        checked text
        )
    """)
    conn.commit()
    conn.close()
    
def add_handle(handle): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "INSERT INTO handles (handle, checked) VALUES (?, ?)"
    values = (handle, 'unchecked')
    cursor.execute(query, values)
    c.commit()
    c.close()

def delete_handle(handle): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    handle_to_delete = handle
    delete_query = "DELETE FROM handles WHERE handle = ?"
    cursor.execute(delete_query, (handle_to_delete,))   
    c.commit()
    c.close()

def get_unchecked_handles(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM handles WHERE checked = ?"
    cursor.execute(query, ('unchecked',))
    rows = cursor.fetchall()
    c.close()
    return rows

def get_checked_handles(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM handles"
    cursor.execute(query)
    rows = cursor.fetchall()
    c.close()
    return rows

def validate_handle(handle): 
    if len(handle) < 3:
        return False
    for char in handle:
        if char not in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_0987654321." :
            return False
    return True