import sqlite3
import os

def init_db(): 
    conn = sqlite3.connect('handle.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS handles (
        handle text, 
        checked text
        )
    """)
    c.execute("""CREATE TABLE IF NOT EXISTS har (
        har text
        )
    """)
    conn.commit()
    conn.close()

def get_har(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "SELECT * FROM har"
    cursor.execute(query)
    c.commit()
    rows = cursor.fetchall()
    c.close()
    return rows

def delete_har(): 
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "DELETE * FROM har"
    cursor.execute(query)
    c.commit()
    c.close()    
    
def add_har(har): 
    delete_har()
    harToText = str(har)
    c = sqlite3.connect('handle.db')
    cursor = c.cursor()
    query = "INSERT INTO har (har) VALUES (?)"
    cursor.execute(query, [harToText])
    c.commit()
    c.close()



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

def validate_har(file_path):
    file_name = os.path.basename(file_path)
    if file_name.endswith('.har') and "youtube.com" in file_name:
        return True
    else:
        return False